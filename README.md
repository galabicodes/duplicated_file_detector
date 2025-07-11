# duplicated_file_detector
Detects and moves duplicate files from a folder to a separate "duplicates" folder using file hash comparison.
This system prevents file clutter and helps organize storage cleanly without touching original non-duplicate files.
## How It Works
Scans a folder and checks every file.
Reads the file content in binary and generates a unique MD5 hash.
If another file has the same hash, it’s marked as duplicate.
All duplicates are moved to a folder called "duplicates" inside the scanned folder.
## Why It’s Powerful
Memory efficient: Uses hashes to compare content, not names.
Safe: Won’t delete, just moves duplicates to a folder.
Clean management: Easy to see what was duplicate without losing data.
