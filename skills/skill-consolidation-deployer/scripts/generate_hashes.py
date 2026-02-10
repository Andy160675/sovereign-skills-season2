#!/usr/bin/env python3
"""Generate SHA-256 hashes for all files in a directory. Outputs hash manifest."""
import os
import hashlib
import json
import sys
from datetime import datetime, timezone

def generate_hashes(directory, output_manifest=None):
    results = []
    for root, _, files in sorted(os.walk(directory)):
        for file in sorted(files):
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, directory)
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            results.append({'file': rel_path, 'sha256': file_hash})
            print(f'{file_hash}  {rel_path}')

    if output_manifest:
        manifest = {
            'generated': datetime.now(timezone.utc).isoformat(),
            'directory': os.path.abspath(directory),
            'file_count': len(results),
            'artifacts': results,
        }
        os.makedirs(os.path.dirname(output_manifest), exist_ok=True)
        with open(output_manifest, 'w') as f:
            json.dump(manifest, f, indent=2)
        print(f'\nManifest written to {output_manifest}')

    return results

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python generate_hashes.py <directory> [manifest.json]')
        sys.exit(1)
    directory = sys.argv[1]
    manifest = sys.argv[2] if len(sys.argv) > 2 else None
    generate_hashes(directory, manifest)
