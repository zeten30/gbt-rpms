#!/bin/bash

rm -rf src/gbt 2>/dev/null

git clone https://github.com/jtyr/gbt src/gbt

GOPATH=$(pwd)/src/gbt
export GOPATH

go get github.com/jtyr/gbt/cmd/gbt
go install github.com/jtyr/gbt/cmd/gbt

cd src || exit 1

tar cfz gbt.tar.gz gbt

cd ..
