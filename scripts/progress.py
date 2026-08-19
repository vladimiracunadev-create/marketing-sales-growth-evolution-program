from pathlib import Path
root=Path(__file__).resolve().parents[1]
parts=sorted(root.glob('curriculum/part-*'))
print('Marketing, Sales & Growth Evolution Program')
for p in parts:
    count=len(list(p.glob('class-*.md')))
    print(f'{p.name}: {count}/14 class files')
