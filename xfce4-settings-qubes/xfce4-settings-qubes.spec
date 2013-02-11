Name:		xfce4-settings-qubes
Version:	1.0
Release:	1%{?dist}
Summary:	Default Xfce4 panel settings for Qubes

Group:		User Interface/Desktops
License:	GPLv2+
URL:		http://www.qubes-os.org/
Source0:	xfce4-panel-qubes-default.xml
Source1:	inhibit-systemd-power-handling.desktop

Requires:	xfce4-panel
Requires(post):	xfce4-panel

%description
%{summary}

%prep

%build


%install
install -D %{SOURCE0} %{buildroot}/etc/xdg/xfce4/panel/qubes-default.xml
install -D %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/inhibit-systemd-power-handling.desktop

%post
if [ -r /etc/xdg/xfce4/panel/default.xml ! -r /etc/xdg/xfce4/panel/xfce4-default.xml ]; then
	mv -f /etc/xdg/xfce4/panel/default.xml /etc/xdg/xfce4/panel/xfce4-default.xml
fi
cp -f /etc/xdg/xfce4/panel/qubes-default.xml /etc/xdg/xfce4/panel/default.xml

%triggerin -- xfce4-panel
if [ -r /etc/xdg/xfce4/panel/default.xml ! -r /etc/xdg/xfce4/panel/xfce4-default.xml ]; then
	mv -f /etc/xdg/xfce4/panel/default.xml /etc/xdg/xfce4/panel/xfce4-default.xml
fi
cp -f /etc/xdg/xfce4/panel/qubes-default.xml /etc/xdg/xfce4/panel/default.xml

%files
/etc/xdg/xfce4/panel/qubes-default.xml
%{_sysconfdir}/xdg/autostart/inhibit-systemd-power-handling.desktop


%changelog

