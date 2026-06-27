#!/usr/bin/env node
'use strict';

function main() {
  const inputPath = process.argv[2];
  const outputPath = process.argv[3];
  if (!inputPath || !outputPath) {
    console.error('Usage: node ua-arch-analyze.js <input.json> <output.json>');
    process.exit(1);
  }

  const fs = require('fs');
  const data = JSON.parse(fs.readFileSync(inputPath, 'utf8'));
  const fileNodes = data.fileNodes || [];
  const importEdges = data.importEdges || [];
  const allEdges = data.allEdges || [];

  const byId = new Map();
  for (const n of fileNodes) byId.set(n.id, n);

  // ---- A. Directory grouping ----
  const paths = fileNodes.map((n) => (n.filePath || '').replace(/\\/g, '/'));

  // common path prefix (directory-segment based)
  function commonPrefix(ps) {
    if (ps.length === 0) return '';
    const split = ps.map((p) => p.split('/'));
    // only consider files that have at least one dir
    const minLen = Math.min(...split.map((s) => s.length));
    const prefix = [];
    for (let i = 0; i < minLen - 1; i++) {
      const seg = split[0][i];
      if (split.every((s) => s[i] === seg)) prefix.push(seg);
      else break;
    }
    return prefix.length ? prefix.join('/') + '/' : '';
  }
  const prefix = commonPrefix(paths);

  function topGroup(filePath) {
    let p = (filePath || '').replace(/\\/g, '/');
    if (prefix && p.startsWith(prefix)) p = p.slice(prefix.length);
    const parts = p.split('/');
    if (parts.length === 1) return '(root)';
    return parts[0];
  }

  const directoryGroups = {};
  const groupOf = new Map();
  for (const n of fileNodes) {
    const grp = topGroup(n.filePath);
    (directoryGroups[grp] = directoryGroups[grp] || []).push(n.id);
    groupOf.set(n.id, grp);
  }

  // ---- B. Node type grouping ----
  const nodeTypeGroups = {};
  for (const n of fileNodes) {
    (nodeTypeGroups[n.type] = nodeTypeGroups[n.type] || []).push(n.id);
  }

  // ---- C. Import adjacency: fan-in / fan-out ----
  const fanOut = {};
  const fanIn = {};
  for (const n of fileNodes) { fanOut[n.id] = 0; fanIn[n.id] = 0; }
  for (const e of importEdges) {
    if (fanOut[e.source] !== undefined) fanOut[e.source]++;
    if (fanIn[e.target] !== undefined) fanIn[e.target]++;
  }

  // ---- D. Cross-category dependency analysis (allEdges by type-pair) ----
  const crossMap = new Map();
  for (const e of allEdges) {
    const s = byId.get(e.source);
    const t = byId.get(e.target);
    if (!s || !t) continue;
    if (s.type === t.type && s.type === 'file') continue; // skip pure file->file noise for cross-category
    const key = s.type + '|' + t.type + '|' + e.type;
    crossMap.set(key, (crossMap.get(key) || 0) + 1);
  }
  const crossCategoryEdges = [];
  for (const [key, count] of crossMap) {
    const [fromType, toType, edgeType] = key.split('|');
    crossCategoryEdges.push({ fromType, toType, edgeType, count });
  }
  crossCategoryEdges.sort((a, b) => b.count - a.count);

  // ---- E. Inter-group import frequency ----
  const interMap = new Map();
  for (const e of importEdges) {
    const a = groupOf.get(e.source);
    const b = groupOf.get(e.target);
    if (a === undefined || b === undefined) continue;
    if (a === b) continue;
    const key = a + '||' + b;
    interMap.set(key, (interMap.get(key) || 0) + 1);
  }
  const interGroupImports = [];
  for (const [key, count] of interMap) {
    const [from, to] = key.split('||');
    interGroupImports.push({ from, to, count });
  }
  interGroupImports.sort((a, b) => b.count - a.count);

  // ---- F. Intra-group import density ----
  const intraGroupDensity = {};
  for (const grp of Object.keys(directoryGroups)) {
    intraGroupDensity[grp] = { internalEdges: 0, totalEdges: 0, density: 0 };
  }
  for (const e of importEdges) {
    const a = groupOf.get(e.source);
    const b = groupOf.get(e.target);
    if (a !== undefined) { intraGroupDensity[a].totalEdges++; if (a === b) intraGroupDensity[a].internalEdges++; }
    if (b !== undefined && b !== a) { intraGroupDensity[b].totalEdges++; }
  }
  for (const grp of Object.keys(intraGroupDensity)) {
    const d = intraGroupDensity[grp];
    d.density = d.totalEdges ? +(d.internalEdges / d.totalEdges).toFixed(3) : 0;
  }

  // ---- G. Directory pattern matching ----
  const dirPatterns = [
    [['routes', 'api', 'controllers', 'endpoints', 'handlers', 'controller', 'routers', 'serializers', 'blueprints'], 'api'],
    [['services', 'core', 'lib', 'domain', 'logic', 'signals', 'internal', 'composables', 'mailers', 'jobs', 'channels'], 'service'],
    [['models', 'db', 'data', 'persistence', 'repository', 'entities', 'migrations', 'entity'], 'data'],
    [['components', 'views', 'pages', 'ui', 'layouts', 'screens'], 'ui'],
    [['middleware', 'plugins', 'interceptors', 'guards'], 'middleware'],
    [['utils', 'helpers', 'common', 'shared', 'tools', 'templatetags', 'pkg'], 'utility'],
    [['config', 'constants', 'env', 'settings', 'management', 'commands'], 'config'],
    [['__tests__', 'test', 'tests', 'spec', 'specs'], 'test'],
    [['types', 'interfaces', 'schemas', 'contracts', 'dtos', 'dto', 'request', 'response'], 'types'],
    [['hooks'], 'hooks'],
    [['store', 'state', 'reducers', 'actions', 'slices'], 'state'],
    [['assets', 'static', 'public'], 'assets'],
    [['cmd', 'bin'], 'entry'],
    [['docs', 'documentation', 'wiki'], 'documentation'],
    [['deploy', 'deployment', 'infra', 'infrastructure', 'k8s', 'kubernetes', 'helm', 'charts', 'terraform', 'tf', 'docker'], 'infrastructure'],
    [['.github', '.gitlab', '.circleci'], 'ci-cd'],
    [['sql', 'database', 'schema'], 'data'],
  ];
  const patternMatches = {};
  for (const grp of Object.keys(directoryGroups)) {
    const lower = grp.toLowerCase();
    let label = null;
    for (const [names, lbl] of dirPatterns) {
      if (names.includes(lower)) { label = lbl; break; }
    }
    if (label) patternMatches[grp] = label;
  }

  // file-level pattern helpers
  function fileLabel(n) {
    const fp = (n.filePath || '').replace(/\\/g, '/');
    const name = n.name || fp.split('/').pop();
    if (/\.(test|spec)\.[a-z]+$/.test(name) || /^test_.*\.py$/.test(name) || /_test\.go$/.test(name) || /Test\.java$/.test(name) || /_spec\.rb$/.test(name) || /Test\.php$/.test(name) || /Tests\.cs$/.test(name)) return 'test';
    if (/\.d\.ts$/.test(name)) return 'types';
    if (/\.(graphql|gql|proto)$/.test(name)) return 'types';
    if (/\.sql$/.test(name)) return 'data';
    if (/\.(md|rst)$/.test(name)) return 'documentation';
    if (name === 'Dockerfile' || /^docker-compose\..*/.test(name)) return 'infrastructure';
    if (/\.(tf|tfvars)$/.test(name)) return 'infrastructure';
    if (name === 'Makefile') return 'infrastructure';
    if (/^(README|AGENTS|TECHNICAL|CONTRIBUTING|CHANGELOG)/i.test(name) && /\.md$/i.test(name)) return 'documentation';
    return null;
  }

  // ---- H. Deployment topology ----
  const allPaths = fileNodes.map((n) => ({ id: n.id, fp: (n.filePath || '').replace(/\\/g, '/'), name: n.name, type: n.type }));
  const infraFiles = [];
  let hasDockerfile = false, hasCompose = false, hasK8s = false, hasTerraform = false, hasCI = false;
  for (const f of allPaths) {
    const nm = f.name || f.fp.split('/').pop();
    if (nm === 'Dockerfile' || /Dockerfile/.test(nm)) { hasDockerfile = true; infraFiles.push(f.fp); }
    else if (/^docker-compose/.test(nm)) { hasCompose = true; infraFiles.push(f.fp); }
    else if (/\.(ya?ml)$/.test(nm) && /(k8s|kubernetes|deployment|manifest)/i.test(f.fp)) { hasK8s = true; infraFiles.push(f.fp); }
    else if (/\.(tf|tfvars)$/.test(nm)) { hasTerraform = true; infraFiles.push(f.fp); }
    else if (/(\.github\/workflows|\.gitlab-ci|Jenkinsfile)/i.test(f.fp)) { hasCI = true; infraFiles.push(f.fp); }
  }
  const deploymentTopology = { hasDockerfile, hasCompose, hasK8s, hasTerraform, hasCI, infraFiles };

  // ---- I. Data pipeline ----
  const schemaFiles = [], migrationFiles = [], dataModelFiles = [], apiHandlerFiles = [];
  for (const f of allPaths) {
    const fp = f.fp;
    if (/\.(sql|graphql|gql|proto|prisma)$/.test(fp)) schemaFiles.push(fp);
    if (/migration/i.test(fp) && /\.sql$/.test(fp)) migrationFiles.push(fp);
    if (/(\/models?\/|\/schemas?\/|\/entities?\/)/i.test(fp)) dataModelFiles.push(fp);
    if (/(\/routes?\/|\/api\/|\/controllers?\/|\/endpoints?\/)/i.test(fp)) apiHandlerFiles.push(fp);
  }
  const dataPipeline = { schemaFiles, migrationFiles, dataModelFiles, apiHandlerFiles };

  // ---- J. Documentation coverage ----
  const docFilesByGroup = {};
  for (const n of fileNodes) {
    if (n.type === 'document' || /\.(md|rst)$/.test(n.name || '')) {
      const grp = groupOf.get(n.id);
      docFilesByGroup[grp] = (docFilesByGroup[grp] || 0) + 1;
    }
  }
  const allGroups = Object.keys(directoryGroups);
  const groupsWithDocs = allGroups.filter((g) => docFilesByGroup[g]).length;
  const undocumentedGroups = allGroups.filter((g) => !docFilesByGroup[g]);
  const docCoverage = {
    groupsWithDocs,
    totalGroups: allGroups.length,
    coverageRatio: allGroups.length ? +(groupsWithDocs / allGroups.length).toFixed(2) : 0,
    undocumentedGroups,
  };

  // ---- K. Dependency direction ----
  const pairNet = new Map();
  for (const { from, to, count } of interGroupImports) {
    const key = [from, to].sort().join('||');
    const cur = pairNet.get(key) || {};
    cur[from + '>' + to] = count;
    pairNet.set(key, cur);
  }
  const dependencyDirection = [];
  for (const [key, dirs] of pairNet) {
    const [a, b] = key.split('||');
    const ab = dirs[a + '>' + b] || 0;
    const ba = dirs[b + '>' + a] || 0;
    if (ab > ba) dependencyDirection.push({ dependent: a, dependsOn: b });
    else if (ba > ab) dependencyDirection.push({ dependent: b, dependsOn: a });
  }

  // ---- file stats ----
  const filesPerGroup = {};
  for (const g of Object.keys(directoryGroups)) filesPerGroup[g] = directoryGroups[g].length;
  const nodeTypeCounts = {};
  for (const t of Object.keys(nodeTypeGroups)) nodeTypeCounts[t] = nodeTypeGroups[t].length;

  // file-level pattern matches (per-file overrides for ambiguous groups)
  const fileLabels = {};
  for (const n of fileNodes) {
    const lbl = fileLabel(n);
    if (lbl) fileLabels[n.id] = lbl;
  }

  const out = {
    scriptCompleted: true,
    commonPrefix: prefix,
    directoryGroups,
    nodeTypeGroups,
    crossCategoryEdges,
    interGroupImports,
    intraGroupDensity,
    patternMatches,
    fileLabels,
    deploymentTopology,
    dataPipeline,
    docCoverage,
    dependencyDirection,
    fileStats: {
      totalFileNodes: fileNodes.length,
      filesPerGroup,
      nodeTypeCounts,
    },
    fileFanIn: fanIn,
    fileFanOut: fanOut,
  };

  fs.writeFileSync(outputPath, JSON.stringify(out, null, 2));
  console.log('Analysis complete. Groups:', Object.keys(directoryGroups).length, 'Total file nodes:', fileNodes.length);
}

try {
  main();
} catch (err) {
  console.error('FATAL:', err && err.stack ? err.stack : err);
  process.exit(1);
}
