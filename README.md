
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
	<META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=utf-8">
	<META NAME="GENERATOR" CONTENT="LibreOffice 4.1.6.2 (Linux)">
	<META NAME="AUTHOR" CONTENT="Froilan Leiza">
	<META NAME="CREATED" CONTENT="20201011;91000000000000">
	<META NAME="CHANGEDBY" CONTENT="Froilan Leiza">
	<META NAME="CHANGED" CONTENT="20201011;121000000000000">
	<META NAME="AppVersion" CONTENT="16.0000">
	<META NAME="DocSecurity" CONTENT="0">
	<META NAME="HyperlinksChanged" CONTENT="false">
	<META NAME="LinksUpToDate" CONTENT="false">
	<META NAME="ScaleCrop" CONTENT="false">
	<META NAME="ShareDoc" CONTENT="false">
</HEAD>
<BODY LANG="en-US" LINK="#0563c1" DIR="LTR">
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="blue"><FONT FACE="Courier New, serif"><FONT SIZE=18 STYLE="font-size: 22pt"><B>Hello
World Scripts</B></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>This
repository was created to store scripts for my Cisco DevNet Associate
Exam v1.0 (DEVASC 200-901) studies. It is a collection of code
samples that make use of Python’s existing frameworks - Netmiko,
Napalm, Nornir, and APIs(NETCONF,RESTCONF, NX API) and some external
API samples.</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=16><B>Requirements</B></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>Jinja2==2.11.2</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>napalm==3.1.0</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>ncclient==0.6.9</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>netmiko==3.2.0</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>nornir==3.0.0</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>nornir-napalm==0.1.1</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>nornir-netmiko==0.1.1</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>nornir-utils==0.1.0</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>pandas==1.1.2</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>paramiko==2.6.0</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>PyYAML==5.3.1</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>requests==2.22.0</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>xmltodict==0.12.0</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=16><B>Environment/Tools
Used To Test Codes</B></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>Operating
System - Ubuntu 20.04.1 LTS</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 </FONT><A HREF="https://ubuntu.com/download/desktop"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://ubuntu.com/download/desktop</FONT></FONT></A></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>EVE-NG
- To emulate Cisco 7200 and CSR1000V routers</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 </FONT><A HREF="https://www.eve-ng.net/index.php/download"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://www.eve-ng.net/index.php/download</FONT></FONT></A></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><A NAME="_GoBack"></A>
<BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>CISSHGO
- To emulate fake routers</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 </FONT><A HREF="https://github.com/tbotnz/cisshgo"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://github.com/tbotnz/cisshgo</FONT></FONT></A></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>Cisco
DevNet Sandbox - Uses Cisco Always-On Sandbox to test
NETCONF/RESTCONF/NX API Codes</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 </FONT><A HREF="https://developer.cisco.com/site/sandbox"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://developer.cisco.com/site/sandbox</FONT></FONT></A></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=16><B>Usage/Installation
Instructions</B></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>Clone
Repository</B></I></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 <FONT FACE="Courier New, serif"><FONT SIZE=2>git clone
</FONT></FONT></FONT><A HREF="https://github.com/leizafroilan/python-hello-world"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://github.com/leizafroilan/python-hello-world</FONT></FONT></A></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 <FONT FACE="Courier New, serif"><FONT SIZE=2>cd DevNet</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 <FONT FACE="Courier New, serif"><FONT SIZE=2>pip install -r
requirements.txt</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>Install
EVE-NG</B></I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>
- </FONT></FONT></FONT><A HREF="https://www.eve-ng.net/index.php/download/"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://www.eve-ng.net/index.php/download/</FONT></FONT></A></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 <FONT FACE="Courier New, serif"><FONT SIZE=2>Cisco CSR1000V and 7200
router configurations are found on router-config directory</FONT></FONT></FONT></P><BR>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>Download/Run
Cisshgo</B></I></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 <FONT FACE="Courier New, serif"><FONT SIZE=2>git clone
</FONT></FONT></FONT><A HREF="https://github.com/tbotnz/cisshgo"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://github.com/tbotnz/cisshgo</FONT></FONT></A></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 <FONT FACE="Courier New, serif"><FONT SIZE=2>sudo snap install go
--classic</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 <FONT FACE="Courier New, serif"><FONT SIZE=2>go run cisshgo/cissh.go</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>Nornir
Scripts</B></I></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="blue"><FONT FACE="Courier New, serif"><FONT SIZE=2>nornir-backup-show-cmd.py
</FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>-
code to backup router and run show commands</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 <FONT FACE="Courier New, serif"><FONT SIZE=2><I>nornir-backup-show-cmd
-h</I></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 <FONT FACE="Courier New, serif"><FONT SIZE=2><I>nornir-backup-show-cmd
backup</I></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000">
 <FONT FACE="Courier New, serif"><FONT SIZE=2><I>nornir-backup-show-cmd
&lt;show commands&gt;</I></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="blue"><FONT FACE="Courier New, serif"><FONT SIZE=2>nornir-jinja-interface-config.py
</FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>-
used jinja2 templates to push interface config to routers (script
currently filters only csv1000v groups)</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="blue"><FONT FACE="Courier New, serif"><FONT SIZE=2>nornir-runbook.py
</FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>-
code that loads, generates configuration files specific to each
devices, runs backup and pushes interface configuration</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>Napalm
Scripts</B></I></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="blue"><FONT FACE="Courier New, serif"><FONT SIZE=2>napalm-1.py</FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>,
</FONT></FONT></FONT><FONT COLOR="blue"><FONT FACE="Courier New, serif"><FONT SIZE=2>napalm-2.py,
napalm-push-acl.py </FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>-
codes to run show commands, generates, loads config files and runs
backup</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="blue"><FONT FACE="Courier New, serif"><FONT SIZE=2>p-mthreading-napalm.py
</FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>-
code to demonstrate multi-threading with pool</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>Netmiko
Scripts</B></I></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="blue"><FONT FACE="Courier New, serif"><FONT SIZE=2>netmiko-1.py,
netmiko-2.py </FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>-
sample codes</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="blue"><FONT FACE="Courier New, serif"><FONT SIZE=2>mthreading-netmiko.py,
p-mthreading-netmiko.py </FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>-
code to demonstrate multi-threading, and multi-threading with pools</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>NETCONF/NX
API Scripts</B></I></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="blue"><FONT FACE="Courier New, serif"><FONT SIZE=2>netconf-1,
nx-api-config-vlan.py, nx-api-show-cmds.py, nx-api-show-interfaces.py
</FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>-
sample codes that demonstrate NETCONF and NX API using requests
library</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>Some
external APIs I created for fun are saved on</FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I>
</I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>sample_requests_api</B></I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I>
</I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>directory</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>Initial
scripts are stored on </FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>initial_scripts</B></I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I>
</I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>directory</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>Function/Modules
used on main scripts are saved on</FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I>
</I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>python_lib</B></I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I>
</I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>directory</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>Input/Output
files, templates are saved on</FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I>
</I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>txtfiles</B></I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I>
and </I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>templates</B></I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I>
</I></FONT></FONT></FONT><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>directories</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2><I><B>Environment
Variables/Paths on ~/.bash_profile or ~/.bashrc</B></I></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:/home/admin/DevNet&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:/home/admin/DevNet/initial_scripts&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:/home/admin/DevNet/work_related&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:/home/admin/DevNet/cisco_netconf_restconf_nx_api&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:/home/admin/DevNet/netmiko&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:/home/admin/DevNet/napalm&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:/home/admin/DevNet/nornir&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:/home/admin/DevNet/sample_requests_api&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:/home/admin/DevNet/python_lib&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:PWD&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:/usr/bin/python3&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PATH=&quot;$PATH:/home/admin/.local/bin&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
PYTHONPATH=&quot;/home/admin/DevNet/python_lib&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
workdir=&quot;/home/admin/DevNet/txtfiles&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
RT_USERNAME=&quot;admin&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=2>export
RT_PASS=&quot;cisco&quot;</FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><FONT COLOR="#000000"><FONT FACE="Courier New, serif"><FONT SIZE=16><B>Credits
and References</B></FONT></FONT></FONT></P>
<P STYLE="margin-bottom: 0in; line-height: 100%"><BR>
</P>
<OL>
	<LI><P STYLE="margin-bottom: 0in; line-height: 100%"><A HREF="https://cisco.developer.com"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://cisco.developer.com</FONT></FONT></A></P>
	<LI><P STYLE="margin-bottom: 0in; line-height: 100%"><A HREF="https://www.youtube.com/redirect?redir_token=QUFFLUhqbERJV09Oc0ZRZ3dfekgtWUlwQklRdFJvTExsd3xBQ3Jtc0ttZjllOVpYc0dIZUVOS05oZnlyNmd3Z3lUV3djQmQ2ejlGSnV5WTREVWZIV2RmMEplWnNGaEN5dS1vMmx3Y0FCUVRaMHNYMmRZZFpzZGVZakVheVlaRDFLWkhGbTVHYmxUa1E2NVp2Tk5HeEVXcTlxOA%3D%3D&amp;v=4NP73RrGacE&amp;q=https%3A%2F%2Fgithub.com%2Ftbotnz%2Fcisshgo&amp;event=video_description"><FONT FACE="Courier New, serif"><FONT SIZE=2><SPAN STYLE="background: #f9f9f9">https://github.com/tbotnz/cisshgo</SPAN></FONT></FONT></A></P>
	<LI><P STYLE="margin-bottom: 0.11in"><A HREF="https://www.eve-ng.net"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://www.eve-ng.net</FONT></FONT></A></P>
	<LI><P STYLE="margin-bottom: 0.11in"><A HREF="https://www.python.org"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://www.python.org</FONT></FONT></A></P>
	<LI><P STYLE="margin-bottom: 0.11in"><A HREF="https://github.com/ktbyers/netmiko"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://github.com/ktbyers/netmiko</FONT></FONT></A></P>
	<LI><P STYLE="margin-bottom: 0.11in"><A HREF="https://github.com/napalm-automation/napalm"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://github.com/napalm-automation/napalm</FONT></FONT></A></P>
	<LI><P STYLE="margin-bottom: 0.11in"><A HREF="https://github.com/nornir-automation/nornir"><FONT FACE="Courier New, serif"><FONT SIZE=2>https://github.com/nornir-automation/nornir</FONT></FONT></A></P>
</OL>
<P STYLE="margin-bottom: 0.11in"><BR><BR>
</P>
<P STYLE="margin-bottom: 0.11in"><BR><BR>
</P>
<P STYLE="margin-bottom: 0.11in"><BR><BR>
</P>
</BODY>
</HTML>

