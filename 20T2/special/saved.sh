test -d "a/b" || mkdir "a/b"
test -f "a/file1" || echo -n "hello andrew
" > "a/file1"
test -d "a/b/c" || mkdir "a/b/c"
test -f "a/b/file2" || echo -n "bye andrew
" > "a/b/file2"
test -f "a/b/c/two" || echo -n "2
" > "a/b/c/two"
test -f "a/b/c/one" || echo -n "1
" > "a/b/c/one"
