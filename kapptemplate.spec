#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kapptemplate
Version  : 18.12.3
Release  : 5
URL      : https://download.kde.org/stable/applications/18.12.3/src/kapptemplate-18.12.3.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.3/src/kapptemplate-18.12.3.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.3/src/kapptemplate-18.12.3.tar.xz.sig
Summary  : KDE Template Generator
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kapptemplate-bin = %{version}-%{release}
Requires: kapptemplate-data = %{version}-%{release}
Requires: kapptemplate-license = %{version}-%{release}
Requires: kapptemplate-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
How To Build This Template
-=-=-=-=-=-=-=-=-=-=-=-=-=
--- On Unix:
cd <project_name_path>
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$KDEDIRS -DCMAKE_BUILD_TYPE=Debug ..
make
make install  or  su -c 'make install'  or  sudo make install

%package bin
Summary: bin components for the kapptemplate package.
Group: Binaries
Requires: kapptemplate-data = %{version}-%{release}
Requires: kapptemplate-license = %{version}-%{release}

%description bin
bin components for the kapptemplate package.


%package data
Summary: data components for the kapptemplate package.
Group: Data

%description data
data components for the kapptemplate package.


%package doc
Summary: doc components for the kapptemplate package.
Group: Documentation

%description doc
doc components for the kapptemplate package.


%package license
Summary: license components for the kapptemplate package.
Group: Default

%description license
license components for the kapptemplate package.


%package locales
Summary: locales components for the kapptemplate package.
Group: Default

%description locales
locales components for the kapptemplate package.


%prep
%setup -q -n kapptemplate-18.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555322204
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555322204
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kapptemplate
cp COPYING %{buildroot}/usr/share/package-licenses/kapptemplate/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kapptemplate/COPYING.DOC
cp src/templates/C++/kde-frameworks5/COPYING %{buildroot}/usr/share/package-licenses/kapptemplate/src_templates_C++_kde-frameworks5_COPYING
cp src/templates/C++/kde-frameworks5/COPYING.DOC %{buildroot}/usr/share/package-licenses/kapptemplate/src_templates_C++_kde-frameworks5_COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang kapptemplate

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kapptemplate

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kapptemplate.desktop
/usr/share/config.kcfg/kapptemplate.kcfg
/usr/share/icons/hicolor/128x128/apps/kapptemplate.png
/usr/share/icons/hicolor/16x16/apps/kapptemplate.png
/usr/share/icons/hicolor/22x22/apps/kapptemplate.png
/usr/share/icons/hicolor/32x32/apps/kapptemplate.png
/usr/share/icons/hicolor/48x48/apps/kapptemplate.png
/usr/share/icons/hicolor/64x64/apps/kapptemplate.png
/usr/share/icons/hicolor/scalable/apps/kapptemplate.svg
/usr/share/kdevappwizard/templates/kde-frameworks5-simple.tar.bz2
/usr/share/kdevappwizard/templates/kde-frameworks5.tar.bz2
/usr/share/metainfo/org.kde.kapptemplate.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kapptemplate/first-page.png
/usr/share/doc/HTML/ca/kapptemplate/fourth-page.png
/usr/share/doc/HTML/ca/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/ca/kapptemplate/index.docbook
/usr/share/doc/HTML/ca/kapptemplate/second-page.png
/usr/share/doc/HTML/ca/kapptemplate/third-page.png
/usr/share/doc/HTML/de/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/de/kapptemplate/index.docbook
/usr/share/doc/HTML/en/kapptemplate/first-page.png
/usr/share/doc/HTML/en/kapptemplate/fourth-page.png
/usr/share/doc/HTML/en/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/en/kapptemplate/index.docbook
/usr/share/doc/HTML/en/kapptemplate/second-page.png
/usr/share/doc/HTML/en/kapptemplate/third-page.png
/usr/share/doc/HTML/es/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/es/kapptemplate/index.docbook
/usr/share/doc/HTML/et/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/et/kapptemplate/index.docbook
/usr/share/doc/HTML/it/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/it/kapptemplate/index.docbook
/usr/share/doc/HTML/nl/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/nl/kapptemplate/index.docbook
/usr/share/doc/HTML/pt/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/pt/kapptemplate/index.docbook
/usr/share/doc/HTML/pt_BR/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kapptemplate/index.docbook
/usr/share/doc/HTML/sv/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/sv/kapptemplate/index.docbook
/usr/share/doc/HTML/uk/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/uk/kapptemplate/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kapptemplate/COPYING
/usr/share/package-licenses/kapptemplate/COPYING.DOC
/usr/share/package-licenses/kapptemplate/src_templates_C++_kde-frameworks5_COPYING
/usr/share/package-licenses/kapptemplate/src_templates_C++_kde-frameworks5_COPYING.DOC

%files locales -f kapptemplate.lang
%defattr(-,root,root,-)

