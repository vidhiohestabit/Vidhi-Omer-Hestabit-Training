🟦 DAY 1 — SYSTEM REVERSE ENGINEERING + NODE & TERMINAL
✅ Tasks

sysinfo.js prints:

Hostname

Available Disk Space (GB)

Open Ports (Top 5)

Default Gateway

Logged-in users count

Created shell aliases in .bashrc / .zshrc

Logged Node runtime metrics:

process.cpuUsage()

process.resourceUsage()

📂 Deliverables
sysinfo.js
logs/day1-sysmetrics.json

![alt text](<Screenshot from 2026-02-04 23-34-06.png>)


🟩 DAY 2 — NODE CLI & CONCURRENCY
✅ Tasks

Built CLI tool:

node stats.js --lines <file> --words <file> --chars <file>


Counts lines, words, characters

Processes 3 files in parallel

Generates performance report

⭐ Bonus

Removes duplicate lines

Outputs unique files to output/

📂 Deliverables
stats.js
logs/performance*.json
output/unique-*.txt

🟥 DAY 3 — GIT MASTERY (RESET, REVERT, CHERRY-PICK, STASH)
✅ Tasks

Repository with 10 commits

Introduced syntax error in commit 5

Used git bisect to find breaking commit

Created release branch release/v0.1

Cherry-picked selective commits

Used stash and restored cleanly

📂 Deliverables
bisect-log.txt
cherry-pick-report.md
stash-proof.txt

![alt text](<Screenshot from 2026-02-04 17-51-59.png>)

🟥 DAY 4 — HTTP / API FORENSICS (cURL + POSTMAN)
✅ Tasks

Used curl -v on GitHub API

Extracted:

Rate-limit remaining

ETag

Server header

Pagination analysis

Created Postman collection

Built Node HTTP server:

/ping

/headers

/count

📂 Deliverables
curl-headers.txt
pagination-analysis.md
POSTMAN-collection.json
server.js

🟥 DAY 5 — AUTOMATION & MINI CI PIPELINE
✅ Tasks

healthcheck.sh (runs every 10s)

Pre-commit checks:

.env protection

JS formatting

Log ignore validation

Created bundle with checksum

Scheduled cron job (every 5 min)

📂 Deliverables
healthcheck.sh
bundle-<timestamp>.zip
checksums.sha1


pre-commit hook (failed):

![alt text](<Screenshot from 2026-02-06 23-16-15.png>)

pre-commit hook (passed):

![alt text](<Screenshot from 2026-02-07 08-22-50.png>)

corn job:-

![alt text](<Screenshot from 2026-02-07 08-24-25.png>)



