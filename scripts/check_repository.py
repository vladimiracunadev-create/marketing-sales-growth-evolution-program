from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
classes=list(root.glob('curriculum/part-*/class-*.md'))
labs=list(root.glob('labs/part-*/*.md'))
assess=list(root.glob('assessments/*.md'))
projects=list(root.glob('projects/*.md'))
notebooks=list(root.glob('notebooks/*.ipynb'))
errors=[]
expected={'classes':336,'labs':48,'assessments':24,'projects':12,'notebooks':8}
actual={'classes':len(classes),'labs':len(labs),'assessments':len(assess),'projects':len(projects),'notebooks':len(notebooks)}
for k,v in expected.items():
    if actual[k]!=v: errors.append(f'{k}: expected {v}, got {actual[k]}')
for p in classes:
    t=p.read_text(encoding='utf-8')
    for required in ['Learning outcomes','Worked example','Guided practice','Evidence to submit','Mastery criterion']:
        if required not in t: errors.append(f'{p}: missing {required}')
for p in notebooks:
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{p}: invalid notebook JSON: {e}')
print('Repository counts:',actual)
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK — repository baseline is structurally complete.')
