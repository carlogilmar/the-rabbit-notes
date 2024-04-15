# Git

## References

- https://shop.jcoglan.com/building-git/

## Frontendmasters

Git Workshop
	- Commit
		- Git stores compressed data in a blob data structure:
			- blob identifier
			- size content
			- delimiter \0
			- Content

Write this for get a SHA1 hash for content:
	`echo ‘hello world’ | git hash-object —stdin`

This for get a SHA1 has for content and header:
`echo 'blob 14\0hello world' | openssl sha1`

The blob is store in objects folder
Git stores information in tree (folders) and this contains pointers to trees and blobs and metadata.

Optimizations:
	Git objects are compressed
	Git optimizes compressing this files together into a 	**Packfile**
	A Packfile stores the object and deltas (differences between two versions)
	Packfiles are generate when
			- you have many objects
			- during gc
			- during a push

Commits
	It’s a point to tree and contains metadata:
		Author, commuter, date, message, parent commit

	The tree is a snapshot of the repository
	Commit is a code snapshot

	If you want see the objects, you will see nothing, because the objects are compressed! But you can use `git cat-file -t 890a0` for see the commit’s -type
Or `git cat-file -p` for print the content

You can have three types:
	- Blob
	- Tree
	- Commit

References are pointers to commits.
	- tags
	- branches
	- HEAD

The file .git/refs/heads/master have to point to hash commit.
The file .git/HEAD have this `ref: refs/heads/master`







	- git cat-file -t -p
	- git internals
	- refs/heads/master
	- git ls-files -s
	- git mv
	- git add -p
	- stashing
		- git stash
		- git stash list
		- git stash show stash@
		- git stash apply
		- git stash apply stash@
		- git stash —include-untracked
		- git stash —-all (also ignoring files )
		- git stash save “WIP in progress“
		- git stash branch <optional stash name>
		- git checkout <stash-name> — <filename>
		- git stash pop
		- git stash drop
		- git stash drop stash@
		- git stash clear

