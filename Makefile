# RPM Makefile
RELEASE=31

sources: clean
	./sources.sh

clean:
	rm -rf rpmbuild/*.*
	rm -rf src/*.tar.gz
	rm -rf src/gbt

srpm: clean sources
	mock -r fedora-$(RELEASE)-x86_64 --spec gbt.spec --sources src/ --resultdir rpmbuild/ --buildsrpm


rpm: srpm
	mock -r fedora-$(RELEASE)-x86_64 --rebuild rpmbuild/gbt-*.src.rpm --resultdir rpmbuild/


copr: srpm
	copr-cli build mzink/Utils rpmbuild/gbt-*.src.rpm --nowait
