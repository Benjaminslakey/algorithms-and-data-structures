git filter-branch --env-filter '
WRONG_NAME="bslakey"
NEW_NAME="Benjaminslakey"
NEW_EMAIL="benjaminslakey@gmail.com"

if [ "$GIT_COMMITTER_NAME" = "$WRONG_NAME" ]
then
    export GIT_COMMITTER_NAME="$NEW_NAME"
    export GIT_COMMITTER_EMAIL="$NEW_EMAIL"
fi
if [ "$GIT_AUTHOR_NAME" = "$WRONG_NAME" ]
then
    export GIT_AUTHOR_NAME="$NEW_NAME"
    export GIT_AUTHOR_EMAIL="$NEW_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags