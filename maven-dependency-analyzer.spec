%{?scl:%scl_package maven-dependency-analyzer}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-dependency-analyzer
Version:        1.7
Release:        1.2%{?dist}
Summary:        Maven dependency analyzer
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-dependency-analyzer/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-model)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-project)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  %{?scl_prefix}mvn(org.ow2.asm:asm)

%description
Analyzes the dependencies of a project for undeclared or unused artifacts.

Warning: Analysis is not done at source but bytecode level, then some cases are
not detected (constants, annotations with source-only retention, links in
javadoc) which can lead to wrong result if they are the only use of a
dependency.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
%{summary}

%prep
%setup -n %{pkg_name}-%{version} -q

# Needed for tests only. However, the right groupId:artifactId of jmock in
# Fedora is org.jmock:jmock
%pom_remove_dep jmock:jmock

%build
# org.jmock.core package is needed, we don't have it
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1.7-1.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.7-1.1
- Automated package import and SCL-ization

* Thu May 04 2017 Michael Simacek <msimacek@redhat.com> - 1.7-1
- Update to upstream version 1.7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-4
- Add missing build-requires
- Remove old obsoletes/provides

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Michal Srb <msrb@redhat.com> - 1.6-1
- Update to upstream version 1.6

* Mon Sep 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-1
- Update to upstream version 1.5

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-6
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-4
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-3
- Fix unowned directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-1
- Update to upstream version 1.4

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-7
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-4
- Replace asm2 R with objectweb-asm
- Resolves: rhbz#902641

* Fri Dec 21 2012 Tomas Radej <tradej@redhat.com> - 1.3-3
- Added missing Provides/Obsoletes

* Thu Dec 20 2012 Tomas Radej <tradej@redhat.com> - 1.3-2
- Removed xmvn + reworked building without it

* Tue Dec 18 2012 Tomas Radej <tradej@redhat.com> - 1.3-1
- Initial package
