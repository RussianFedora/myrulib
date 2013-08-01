Name:           myrulib
Version:        0.29.14
Release:        2%{?dist}
Summary:        E-Book Library Manager
Summary(ru):    Каталогизатор электронных книг

License:        GPLv3
URL:            http://myrulib.lintest.ru
Group:          Applications/Publishing
Source0:        http://www.lintest.ru/pub/%{name}-%{version}.tar.bz2

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

%description -l ru
MyRuLib предназначен для организации вашей собственной коллекции электронных
книг.


%prep
%setup -q


%build
%configure \
            --with-expat \
            --with-icu \
            --with-strip
make %{?_smp_mflags}


%install
%make_install
%find_lang %{name}


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
* Thu Aug 01 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.29.14-2.R
- corrected LDFLAGS
- added russian description

* Fri Jul 26 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.29.14-1.R
- update to 0.29.14

* Wed Jun 13 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.29.8-1.R
- update to 0.29.8

* Tue Oct 18 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 0.28.9-2.R
- build without reader

* Fri Oct  7 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 0.28.9-1.R
- initial build
