### Assignment 4:  Create & Merge Pull Request

**Objective:** Perform the professional Pull Request workflow.

**Tasks:**
1. Create a new branch `feature/services-page`.
2. Add a file `services.txt` with any content.
3. Commit the changes.
4. Push the branch using:
   ```bash
   git push -u origin feature/services-page
   ```
5. Go to GitHub and create a Pull Request.
6. Merge the Pull Request.
7. Delete the branch on GitHub.
8. Update your local main:
   ```bash
   git switch main
   git pull origin main
   git branch -d feature/services-page
   ```

**Submission:**  
- Screenshot of the created Pull Request  
- Screenshot after merging the PR  
- Screenshot of final `git log --oneline` on main
