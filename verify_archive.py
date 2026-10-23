"""Offline verification only; standard library, no provider or MT5 imports."""
from pathlib import Path
import hashlib,json,importlib.util,sys
root=Path(__file__).resolve().parent
manifest=json.loads((root/'release_manifest.json').read_text(encoding='utf-8'))
for entry in manifest['files']:
 p=(root/entry['path']).resolve()
 if not p.is_relative_to(root) or not p.is_file():raise ValueError('Missing/escaping release path')
 if p.stat().st_size!=entry['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=entry['sha256']:raise ValueError('Release hash mismatch: '+entry['path'])
spec=importlib.util.spec_from_file_location('stored_artifact_replay',root/'replay/replay.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
result=mod.replay(root/'replay')
print(json.dumps({'status':'PASS_PREPARED_DEPOSIT','release_files':len(manifest['files']),'primary_replay':result,'new_model_calls':0,'independent_researcher_verification':False}))
