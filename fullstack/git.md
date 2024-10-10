### Git Merge vs. Rebase

**Git Merge:**
- Combines changes from two branches.
- Maintains the history of both branches.
- Creates a new "merge commit" that ties together the histories of the merged branches.
- Ideal for preserving the context of the original branches.

**Example:**
```bash
git checkout main
git merge feature-branch
```

**Git Rebase:**
- Moves or combines a sequence of commits to a new base commit.
- Creates a linear history by applying commits from one branch onto another.
- Can simplify the project history but may rewrite commit history, which can be risky if the branch has been shared with others.

**Example:**
```bash
git checkout feature-branch
git rebase main
```

### Key Differences:
- **History:** Merge preserves history; rebase creates a linear history.
- **Commits:** Merge creates a new commit; rebase moves commits.
- **Use Cases:** Use merge for collaborative work; use rebase for cleaner project history.

### When to Use:
- **Merge:** When you want to keep the complete history and context.
- **Rebase:** When you want to streamline the commit history before merging into the main branch. 



Here are answers to the Git interview questions with examples:

1. **What is Git?**
   - **Answer:** Git is a distributed version control system that allows multiple developers to work on a project simultaneously without interfering with each other's changes. It tracks changes in source code during software development.
   - **Example:** When you make changes to a file, you can commit those changes to your local repository, and later push them to a remote repository like GitHub.

2. **What is the difference between `git fetch` and `git pull`?**
   - **Answer:** `git fetch` downloads changes from the remote repository to your local repository but does not merge them. `git pull` does both: it fetches and merges the changes.
   - **Example:**
     ```bash
     git fetch origin
     git pull origin main
     ```

3. **How do you resolve a merge conflict in Git?**
   - **Answer:** When a merge conflict occurs, Git will mark the conflicting areas in the files. You need to manually edit the files to resolve the conflicts and then commit the resolved changes.
   - **Example:**
     ```bash
     git merge feature-branch
     # Conflict occurs
     # Edit the conflicting files
     git add resolved-file.txt
     git commit -m "Resolved merge conflict"
     ```

4. **What is a branch in Git, and how do you create one?**
   - **Answer:** A branch in Git is a pointer to a specific commit, allowing you to work on features or fixes in isolation. You can create a branch using the `git branch` command.
   - **Example:**
     ```bash
     git branch new-feature
     git checkout new-feature
     ```

5. **What does `git rebase` do?**
   - **Answer:** `git rebase` moves or combines a sequence of commits to a new base commit. It helps to keep a clean project history.
   - **Example:**
     ```bash
     git checkout feature-branch
     git rebase main
     ```

6. **What is the purpose of `.gitignore`?**
   - **Answer:** The `.gitignore` file specifies files and directories that Git should ignore, preventing them from being tracked.
   - **Example:** A typical `.gitignore` might include:
     ```
     node_modules/
     *.log
     .env
     ```

7. **How can you view the commit history in Git?**
   - **Answer:** You can view the commit history using the `git log` command, which shows a list of commits, their hashes, and messages.
   - **Example:**
     ```bash
     git log  
     ```

8. **What is the difference between `git reset`, `git checkout`, and `git revert`?**
   - **Answer:**
     - `git reset` moves the HEAD to a specified commit and can modify the index and working directory.
     - `git checkout` is used to switch branches or restore working tree files.
     - `git revert` creates a new commit that undoes the changes made by a previous commit.
   - **Example:**
     ```bash
     git reset HEAD~1  # Undo last commit
     git checkout feature-branch  # Switch branches
     git revert a1b2c3d  # Revert specific commit
     ```

9. **How do you undo a commit that has already been pushed?**
   - **Answer:** You can use `git revert` to create a new commit that undoes the changes of the pushed commit.
   - **Example:**
     ```bash
     git revert HEAD  # Undo the last commit
     git push origin main  # Push the revert commit
     ```

10. **What is a remote repository, and how do you add one?**
    - **Answer:** A remote repository is a version of your project that is hosted on the internet or another network. You can add a remote using `git remote add`.
    - **Example:**
      ```bash
      git remote add origin https://github.com/username/repo.git
      ```

These answers provide a solid foundation for understanding Git and its functionalities.!