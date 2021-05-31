# Rclone Wrapper Status


## Available Commands:

cat             Concatenates any files and sends them to stdout.
check           Checks the files in the source and destination match.
cleanup         Clean up the remote if possible.
config          Enter an interactive configuration session.
copy            Copy files from source to dest, skipping already copied.
copyto          Copy files from source to dest, skipping already copied.
copyurl         Copy url content to dest.
cryptcheck      Cryptcheck checks the integrity of a crypted remote.
cryptdecode     Cryptdecode returns unencrypted file names.
dedupe          Interactively find duplicate filenames and delete/rename them.
delete          Remove the files in path.
deletefile      Remove a single file from remote.
genautocomplete Output completion script for a given shell.
gendocs         Output markdown docs for rclone to the directory supplied.
hashsum         Produces a hashsum file for all the objects in the path.
help            Show help for rclone commands, flags and backends.
link            Generate public link to file/folder.
listremotes     List all the remotes in the config file.
ls              List the objects in the path with size and path.
lsd             List all directories/containers/buckets in the path.
lsf             List directories and objects in remote:path formatted for parsing.
lsjson          List directories and objects in the path in JSON format.
lsl             List the objects in path with modification time, size and path.
md5sum          Produces an md5sum file for all the objects in the path.
mkdir           Make the path if it doesn't already exist.
mount           Mount the remote as file system on a mountpoint.
move            Move files from source to dest.
moveto          Move file or directory from source to dest.
ncdu            Explore a remote with a text based user interface.
obscure         Obscure password for use in the rclone config file.
purge           Remove the path and all of its contents.
rc              Run a command against a running rclone.
rcat            Copies standard input to file on remote.
rcd             Run rclone listening to remote control commands only.
rmdir           Remove the empty directory at path.
rmdirs          Remove empty directories under the path.
selfupdate      Update the rclone binary.
serve           Serve a remote over a protocol.
settier         Changes storage class/tier of objects in remote.
sha1sum         Produces an sha1sum file for all the objects in the path.
size            Prints the total size and number of objects in remote:path.
sync            Make source and dest identical, modifying destination only.
test            Run a test command
touch           Create new file or change file modification time.
tree            List the contents of the remote in a tree like fashion.
version         Show the version number.

## Skipped Commands (not for s3)

- about           Get quota information from the remote.
- authorize       Remote authorization.
- backend         Run a backend specific command.