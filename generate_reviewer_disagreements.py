import pandas as pd
import re
import os

# === 1. Setup ===
cwd = os.getcwd()
input_file = os.path.join(cwd, 'Conflicts_YemiVotes_04062025.csv')

# === 2. Read CSV ===
try:
    df = pd.read_csv(input_file)
    print(f"✅ File loaded: {input_file}")
except FileNotFoundError:
    print("❌ ERROR: File not found.")
    exit()
except Exception as e:
    print(f"❌ ERROR reading file: {e}")
    exit()

# === 3. Extract reviewer votes from notes column ===
def extract_vote(note, reviewer):
    pattern = fr'"{reviewer}"=>"(\w+)"'
    match = re.search(pattern, str(note))
    return match.group(1) if match else None

reviewers = ['Opeyemi', 'Fabian', 'Lauren', 'Jackeline', 'Oshani']
for reviewer in reviewers:
    df[f'{reviewer}_decision'] = df['notes'].apply(lambda x: extract_vote(x, reviewer))

# === 4. Compare reviewers to Opeyemi ===
for reviewer in reviewers:
    if reviewer != 'Opeyemi':
        df[f'{reviewer}_agrees'] = df.apply(
            lambda row: 'Agrees'
            if row['Opeyemi_decision'] == row[f'{reviewer}_decision']
            else 'Disagrees',
            axis=1
        )

# === 5. Generate one file per reviewer (only true disagreements) ===
extra_fields = ['journal', 'authors', 'abstract']
output_folder = cwd  # save in same folder you're running from

for reviewer in reviewers:
    if reviewer == 'Opeyemi':
        continue

    # Filter only where BOTH have voted AND disagree
    disagrees = df[
        (df['Opeyemi_decision'].notna()) &
        (df[f'{reviewer}_decision'].notna()) &
        (df[f'{reviewer}_agrees'] == 'Disagrees')
    ]

    if disagrees.empty:
        print(f"✅ No true disagreements for {reviewer}.")
        continue

    # Select columns for export
    cols = ['key', 'title', 'year'] + extra_fields + ['Opeyemi_decision', f'{reviewer}_decision']
    reviewer_df = disagrees[cols]

    # Save to CSV
    filename = f'{reviewer}_true_disagreements.csv'
    output_path = os.path.join(output_folder, filename)
    reviewer_df.to_csv(output_path, index=False)

    print(f"📁 True disagreements for {reviewer} saved to: {output_path}")
