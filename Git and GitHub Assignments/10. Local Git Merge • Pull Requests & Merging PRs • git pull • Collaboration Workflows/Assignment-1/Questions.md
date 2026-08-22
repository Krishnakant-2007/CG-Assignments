### Assignment 1 – Local Merge (Mandatory)

**Goal:** Practice merging a feature branch into `main` locally.

1. Create a new branch:  
   `git checkout -b feature-local-merge`
2. Create a file named `local-merge.txt` and write 3–4 lines about what you learned today about local merge.
3. Stage and commit:  
   `git add .`  
   `git commit -m "Add local-merge notes"`
4. Switch back to main:  
   `git checkout main`
5. Merge the feature branch:  
   `git merge feature-local-merge`
6. Push main:  
   `git push origin main`
7. Run `git log --oneline -5` and take a screenshot of the history.

**Submit:** Screenshot of `git log --oneline` after the merge + confirmation that the file is on GitHub `main`.
