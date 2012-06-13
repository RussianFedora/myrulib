Summary:        E-Book Library Manager
Name:           myrulib
Version:        0.29.8
Release:        1%{?dist}

License:        GPLv3
URL:            http://myrulib.lintest.ru
Group:          Applications/Publishing
Source0:        http://www.lintest.ru/pub/myrulib-%{version}.tar.bz2

BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  desktop-file-utils
BuildRequires:  wxGTK-devel >= 2.8.10
BuildRequires:  libsqlite3x-devel
BuildRequires:  expat-devel
BuildRequires:  gettext

%description
MyRuLib is an application for organizing your own collection of e-books.
This package includes built-in CoolReader3 engine.


%prep
%setup -q


%build
%configure \
            --with-expat \
            --with-icu \
            --with-strip

make LDFLAGS="-Wl,--add-needed" %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install

%find_lang myrulib


%post
touch --no-create /usr/share/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create /usr/share/icons/hicolor &>/dev/null
    gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :


%files -f myrulib.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog LICENSE README
%{_bindir}/myrulib
%{_datadir}/applications/myrulib.desktop
%{_datadir}/icons/hicolor/*/*/myrulib.png
%{_datadir}/pixmaps/myrulib.png


%changelog
* Wed Jun 13 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.29.8-1.R
- update to 0.29.8

* Tue Oct 18 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 0.28.9-2.R
- build without reader

* Fri Oct  7 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 0.28.9-1.R
- initial build
