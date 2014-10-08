Name:           myrulib
Version:        0.29.16
Release:        1%{?dist}
Summary:        E-Book Library Manager
Summary(ru):    Каталогизатор электронных книг

License:        GPLv3
URL:            http://myrulib.lintest.ru
Group:          Applications/Publishing
Source0:        http://www.lintest.ru/pub/%{name}-%{version}.tar.bz2

BuildRequires:  libjpeg-devel
BuildRequires:  desktop-file-utils
BuildRequires:  wxGTK-devel >= 2.8.10
BuildRequires:  libsqlite3x-devel
BuildRequires:  expat-devel
BuildRequires:  gettext
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils

%description
MyRuLib is an application for organizing your own collection of e-books.
This package includes built-in CoolReader3 engine.

%description -l ru
MyRuLib предназначен для организации вашей собственной коллекции электронных
книг.


%prep
%setup -q
rm -rf 3rdparty/sqlite3
rm -rf 3rdparty/bzip2
rm -rf 3rdparty/bakefile
#rm -rf 3rdparty/bin2c
rm -rf 3rdparty/crengine
rm -rf 3rdparty/expat
rm -rf 3rdparty/faxpp
rm -rf 3rdparty/gnome
#rm -rf 3rdparty/wxbzipstream
#rm -rf 3rdparty/wxsqlite3

%build
%configure \
            --with-expat \
            --without-icu \
            --without-strip \
            --without-sqlite
make 
#%{?_smp_mflags}


%install
%make_install
%find_lang %{name}

desktop-file-validate %buildroot%{_datadir}/applications/%{name}.desktop

%post
touch --no-create /usr/share/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create /usr/share/icons/hicolor &>/dev/null
    gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%doc AUTHORS ChangeLog LICENSE README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_datadir}/pixmaps/%{name}.png


%changelog
* Wed Oct 08 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 0.29.16-1
- Update to 0.29.16

* Mon Aug 12 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.29.14-4
- remove bundled libraries
- validate .desktop file

* Tue Aug 06 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.29.14-3
- added debug info

* Thu Aug 01 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.29.14-2
- corrected LDFLAGS
- added russian description

* Fri Jul 26 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.29.14-1
- update to 0.29.14

* Wed Jun 13 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.29.8-1
- update to 0.29.8

* Tue Oct 18 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 0.28.9-2
- build without reader

* Fri Oct  7 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 0.28.9-1
- initial build
