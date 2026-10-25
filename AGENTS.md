# Repository Instructions

## Working Rules

- Work on a dedicated branch using the `codex/` prefix by default.
- Commit each significant step once it is coherent and verified.
- Use commit messages in the `<type>: <emoji> <message>` format.
- Continue through pushing the feature branch and opening or updating a PR
  unless the user says otherwise or a real blocker prevents it.
- Do not bypass permission failures by changing caches or tool state. Request
  approval for the command that needs access.
- Keep these instructions concise and preserve existing rules when reorganizing.
- Do not add reports of dependency reviews or compatibility findings to the
  repository. Report them in chat and the PR.

## Pull Requests

- Use the GitHub connector for PR metadata, files, diffs, creation and updates.
  Try it before the `gh` CLI; explain the reason if a CLI fallback is necessary.
- Target feature PRs at `develop`. Use draft status until required checks pass.
- Squash merge feature PRs. Never merge a PR without user authorization.
- After an authorized product merge into `develop`, open or update the release
  PR from `develop` to `main`; documentation alone does not trigger a release.
- Use the normal merge behavior for release PRs and title them `Version <version>`
  using the version in `pyproject.toml`.
- After an authorized release merge, return to `develop`, fetch `main` with
  `git fetch origin main:main`, fast-forward with `git merge --ff-only main`,
  and push `develop`.
- Delete merged local feature branches; retain `develop` and `main`.

## Python Tooling and Checks

- Use `uv` for dependency management. Add and remove dependencies with `uv`
  commands; commit `pyproject.toml`, `uv.lock` and the generated requirements.
- Change Python dependencies in the manifest and regenerate the lock. Do not
  edit `uv.lock` or `requirements.txt` by hand.
- Install both hook types after setup or any hook stage changes:

  ```bash
  uv run pre-commit install --hook-type pre-commit --hook-type pre-push
  ```

- Rely on `git commit` for Ruff, djLint, markdownlint, lock/export and hygiene
  hooks. Rely on `git push` for the project check hook. Run tools manually only
  to diagnose a failure or when explicitly requested. CI runs all checks.
- Before opening or updating any dependency PR, require a current lock and
  export, compatible installed dependencies, Django system checks, no missing
  migrations, passing pytest tests and a clean dependency security audit.
- Required CI includes Python 3.14 tests on SQLite and PostgreSQL, all-file
  hooks, and the production container build and smoke check. Python 3.15 is an
  experimental CI job and does not replace the required Python 3.14 checks.
- Keep test settings isolated. Use `TEST_DATABASE_URL` for a disposable test
  database; never use a developer or production database for verification.
- Keep deployment artifacts in Docker and Compose compatible with Dokploy.

## Code Organization

- Keep project settings, URLs and Celery setup in `storefront/`.
- Keep store domain models, serializers, views and tests in `store/`.
- Keep custom user and authentication code in `core/`.
- Keep generic relations in `likes/` and `tags/`, and examples in `playground/`.
- Keep root entry points thin and repository check scripts in `scripts/`.
- Preserve applied migrations. Add new migrations for model state changes.
- Keep exported helpers public; use leading underscores for private details.
- Keep secrets and local environments out of Git.
