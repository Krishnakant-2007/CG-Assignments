### Assignment 2 
**Modify/Delete Conflict**

**Goal:** Create and resolve a Modify/Delete conflict (one branch deletes a file, another branch modifies it).

1. On remote `main`, create a file `notes.txt` with some content and commit it on GitHub.  
   Then update local main:
   ```bash
   git fetch origin main
   git merge origin/main
   ```
2. Create branch `feature/notes-delete`:
   - Delete `notes.txt`
   - Commit and push
   - Open a Pull Request (do **not** merge yet)
3. Create branch `feature/notes-edit` (from main):
   - Edit `notes.txt` and add one extra sentence
   - Commit and push
   - Open a second Pull Request
4. Merge the **delete** PR first.
5. Try to merge the **edit** PR → you will get a complex conflict (may not be resolvable in the web editor).
6. Resolve it **locally**:
   ```bash
   git checkout main
   git pull origin main
   git switch feature/notes-edit
   git merge main
   ```
7. Decide to **keep the file** and write a clear final content.  
   Then:
   ```bash
   git add .
   git commit -m "Resolve modify/delete conflict"
   git push origin feature/notes-edit
   ```
8. Merge the PR on GitHub, delete remote & local feature branches, and run `git pull origin main`.

**Submit:**
- Links to both PRs
- Screenshot of the conflict message / VS Code showing the conflict
- Screenshot of final `notes.txt` on main
- Repository link
