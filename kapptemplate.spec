#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kapptemplate
Version  : 22.12.2
Release  : 48
URL      : https://download.kde.org/stable/release-service/22.12.2/src/kapptemplate-22.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.2/src/kapptemplate-22.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.2/src/kapptemplate-22.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 GPL-3.0
Requires: kapptemplate-bin = %{version}-%{release}
Requires: kapptemplate-data = %{version}-%{release}
Requires: kapptemplate-license = %{version}-%{release}
Requires: kapptemplate-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kapptemplate-22.12.2
cd %{_builddir}/kapptemplate-22.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675653361
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1675653361
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kapptemplate
cp %{_builddir}/kapptemplate-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kapptemplate/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kapptemplate-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kapptemplate/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kapptemplate-%{version}/src/templates/C++/kde-frameworks5-simple/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kapptemplate/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kapptemplate-%{version}/src/templates/C++/kde-frameworks5-simple/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kapptemplate/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kapptemplate-%{version}/src/templates/C++/kde-frameworks5-simple/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kapptemplate/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kapptemplate-%{version}/src/templates/C++/kde-frameworks5-simple/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kapptemplate/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kapptemplate-%{version}/src/templates/C++/kde-frameworks5/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kapptemplate/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kapptemplate-%{version}/src/templates/C++/kde-frameworks5/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kapptemplate/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kapptemplate-%{version}/src/templates/C++/kde-frameworks5/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kapptemplate/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kapptemplate-%{version}/src/templates/C++/kde-frameworks5/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kapptemplate/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kapptemplate-%{version}/src/templates/C++/kde-frameworks5/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kapptemplate/7d9831e05094ce723947d729c2a46a09d6e90275 || :
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
/usr/share/qlogging-categories5/kapptemplate.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/ca/kapptemplate/index.docbook
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
/usr/share/doc/HTML/fr/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/fr/kapptemplate/index.docbook
/usr/share/doc/HTML/it/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/it/kapptemplate/index.docbook
/usr/share/doc/HTML/nl/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/nl/kapptemplate/index.docbook
/usr/share/doc/HTML/pt/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/pt/kapptemplate/index.docbook
/usr/share/doc/HTML/pt_BR/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kapptemplate/index.docbook
/usr/share/doc/HTML/ru/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/ru/kapptemplate/index.docbook
/usr/share/doc/HTML/sv/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/sv/kapptemplate/index.docbook
/usr/share/doc/HTML/uk/kapptemplate/index.cache.bz2
/usr/share/doc/HTML/uk/kapptemplate/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kapptemplate/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kapptemplate/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kapptemplate/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kapptemplate/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kapptemplate/7d9831e05094ce723947d729c2a46a09d6e90275

%files locales -f kapptemplate.lang
%defattr(-,root,root,-)

