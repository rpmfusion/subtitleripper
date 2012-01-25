Summary: 	A tool to rip DVD subtitles
Name: 		subtitleripper
Version: 	0.3.4
Release: 	9%{?dist}
License: 	GPL
Group: 		Applications/Multimedia
URL: 		http://subtitleripper.sourceforge.net/
Source0: 	http://switch.dl.sourceforge.net/sourceforge/subtitleripper/%{name}-%{version}-4.tgz
Patch0:		subtitleripper-0.3-4-nopng.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	netpbm-devel zlib-devel

#-----------------------------------------------------------------------------
%description
Converts DVD subtitles into text format (e.g. subrip format) or VobSub
format. Based on transcode.

#-----------------------------------------------------------------------------
%prep
%setup -q -n %{name}
test -L %{_libdir}/libnetpbm.so && \
	perl -pi -e 's/-lppm/-lnetpbm/g' Makefile
%patch0 -p1 -b .patch0

#-----------------------------------------------------------------------------
%build
CFLAGS="$RPM_OPT_FLAGS" make

#-----------------------------------------------------------------------------
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
for i in pgm2txt srttool subtitle2pgm subtitle2vobsub
do
  install -m 0755 $i $RPM_BUILD_ROOT/%{_bindir}
done

#-----------------------------------------------------------------------------
%clean
rm -rf $RPM_BUILD_ROOT

#-----------------------------------------------------------------------------
%files
%defattr(-,root,root,-)
%doc ChangeLog README*
%{_bindir}/pgm2txt
%{_bindir}/srttool
%{_bindir}/subtitle2pgm
%{_bindir}/subtitle2vobsub

#-----------------------------------------------------------------------------
%changelog
* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.3-7
- rebuild for new F11 features

* Tue Aug 19 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.3-6
- added _default_patch_fuzz define

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.3-5
- rebuild

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Wed Sep 21 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> 0:0.3-0.lvn.4
- Drop BR libpng, too

* Sat Sep 10 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> 0:0.3-0.lvn.3
- Disable png-support for now cause it does not compile on FC4

* Mon Jun 28 2004 Dams <anvil[AT]livna.org> 0:0.3-0.lvn.2.4
- BuildReq libpng-devel
- Fix for libnetpbm on FC2

* Mon Jun 28 2004 Dams <anvil[AT]livna.org> 0:0.3.4-0.lvn.1
- Updated to 0.3-4

* Wed May 14 2003 Dams <anvil[AT]livna.org> 0:0.3-0.fdr.2
- Added missing zlib-devel BuildRequires

* Sat May 10 2003 Dams <anvil[AT]livna.org> 
- Initial build.
