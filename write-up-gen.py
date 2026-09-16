from datetime import date
import os
import subprocess
import sys
import xml.etree.ElementTree as ET

def scan(IP):
    os.makedirs("nmap", exist_ok=True)
    subprocess.run(["nmap", "-sC", "-sV", "-oA", "nmap/scan", "-p-", IP])

def generateReport(date,IP,portList):
    print("generating report...")
    scan = []
    with open("nmap/scan.nmap", "r") as infile:
        scan = infile.readlines()
    
    with open("report.md", "w") as outfile:
        outfile.write("# <Box Name\\> - <Vendor\\>\n")
        outfile.write("**Difficulty:**\n\n")
        outfile.write("**OS:**\n\n")
        outfile.write("**Date Completed:** " + date + "\n\n")
        outfile.write("**Write-up Authored by:** Ian Simons\n\n")
        outfile.write("**Challenge Created by:** \n\n")
        outfile.write("**Core Competencies:** \n\n") 
        outfile.write("- competency 1\n\n")
        outfile.write("- competency 2\n\n")
        outfile.write("- competency 3\n\n---\n")
        outfile.write("### Overview\n")
        outfile.write("<overview of the box, if full report replace with executive summary\\>\n\n---\n")
        outfile.write("### Vulnerability Summary\n")
        outfile.write("\n")
        outfile.write("| Vulnerability | Vulnerability Classification | CVSS Score | MITRE ATT&CK Technique | ATT&CK Tactic|\n|--- | --- | --- | --- | --- |\n\n")
        outfile.write("---\n")
        outfile.write("### Attack Path Summary\n")
        outfile.write("1. step 1\n\n")
        outfile.write("1. step 2\n\n")
        outfile.write("1. step 3\n\n---\n")
        outfile.write("### Reconnaissance\n")
        outfile.write("#### Port Discovery\n")
        outfile.write("Nmap Scan Results\n")
        outfile.write("```\n")
        for i in scan:
            outfile.write(i)
        outfile.write("```\n\n") 
        outfile.write("#### Key Open Ports and Services\n")
        outfile.write("| Port | Service | Version |\n| --- | --- | --- |\n")
        for i in portList:
            if i.state == "open":
                outfile.write("|"+i.portNum+" | "+i.service+" | "+i.version+" |\n")
        outfile.write("\n")
        outfile.write("#### Web Enumeration\n")
        outfile.write("<paragraph detailingweb enumeration on this box\\>\n")
        outfile.write("```\n")
        outfile.write("<GoBuster Scan if Appropriate>\n")
        outfile.write("```\n")
        outfile.write("<GoBuster Interpretation\\>\n\n")
        outfile.write("#### Vulnerability Research\n")
        outfile.write("<paragraph describing vulnerabilites found based on Enumeration\\>\n\n---\n")
        outfile.write("### Initial Access\n")
        outfile.write("#### Vulnerability Details\n")
        outfile.write("**Description:** <comma separated vulnerability common names\\>\n\n")
        outfile.write("**Vulnerability Classification:** <CVE's, CWE's etc\\>\n\n")
        outfile.write("**CVSS Score:** <CVSS scores as applicable\\>\n\n")
        outfile.write("**MITRE ATT&CK:** <ATT&CK Tactic\\> - <MITRE ATT&CK Techniques\\>\n\n")
        outfile.write("<Paragraph explaining how vulnerabilities identified lead to initial access\\>\n\n")
        outfile.write("#### Exploitation Steps\n")
        outfile.write("<Paragraph quickly running through how the exploit was executed\\>\n\n")
        outfile.write("1. step 1 \n\n")
        outfile.write("1. step 2 \n\n")
        outfile.write("1. step 3 \n\n\n")
        outfile.write("#### Key Commands / Payloads\n")
        outfile.write("```\n")
        outfile.write("<List all commands used as well as a comment explaining it>\n\nex:")
        outfile.write("# list folder contents\n\n")
        outfile.write("ls\n\n")
        outfile.write("```\n\n")
        outfile.write("#### Proof of Access\n")
        outfile.write("##### Screen Shots\n")
        outfile.write("<link to image\\>\n\n")
        outfile.write("Figure 1: Proof of initial access. Successful exploitation of <CVE\\> resulted in command execution on the target host. Session validated by confirming the execution context, hostname, and operating system.\n\n")
        outfile.write("##### Session Validation Commands\n")
        outfile.write("```\n")
        outfile.write("<comments explaining commands and all commands used in screenshot\\>\n\n---\n")
        outfile.write("### Privilege Escalation\n")
        outfile.write("#### Vulnerability Details\n")
        outfile.write("**Description:** <comma separated vulnerability common names\\>\n\n")
        outfile.write("**Vulnerability Classification:** <CVE's, CWE's etc\\>\n\n")
        outfile.write("**CVSS Score:** <CVSS scores as applicable\\>\n\n")
        outfile.write("**MITRE ATT&CK:** <ATT&CK Tactic\\> - <MITRE ATT&CK Techniques\\>\n\n")
        outfile.write("<Paragraph explaining how vulnerabilities identified lead to Privilege Escalation\\>\n\n")
        outfile.write("1. step 1 \n\n")
        outfile.write("1. step 2 \n\n")
        outfile.write("1. step 3 \n\n\n")
        outfile.write("#### Key Commands / Payloads\n")
        outfile.write("```\n")
        outfile.write("<List all commands used as well as a comment explaining it>\n\nex:")
        outfile.write("# list folder contents\n\n")
        outfile.write("ls\n\n")
        outfile.write("```\n\n")
        outfile.write("#### Proof of Privilege Escalation\n")
        outfile.write("##### Screen Shots\n")
        outfile.write("<link to image\\>\n\n")
        outfile.write("Figure 2: Proof of Privilege Escalation. Successful exploitation of resulted in execution within the<root/SYSTEM\\> security context. Privileges were validated by confirming the execution context with the `whoami` command.\n\n---\n")
        outfile.write("### Lessons Learned\n")
        outfile.write("<paragraph detailing lessons learned in this box and why it has helped improve skills et\\>\n\n")
        outfile.write("- learning bullet point 1\n\n")
        outfile.write("- learning bullet point 2\n\n")
        outfile.write("- learning bullet point 3\n\n---\n")
        outfile.write("### Appendix\n")
        outfile.write("#### Appendix A\n")
        outfile.write("##### Tools Used\n\n")
        outfile.write("| Tool | Purpose |\n| --- | --- |\n\n")
        outfile.write("#### Appendix B\n")
        outfile.write("##### Flags Found\n")
        outfile.write("<link to flag 1 screenshot\\>\n\n")
        outfile.write("User Flag:\n\n")
        outfile.write("<heavily redacted user flag\\>\n\n")
        outfile.write("<link to flag 2 screenshot\\>\n\n")
        outfile.write("Root Flag:\n\n")
        outfile.write("<heavily redacted root flag\\>\n\n")
        outfile.write("### Appendix C\n")
        outfile.write("#### Supporting Evidence\n")
        outfile.write("<Any other relevant supporting evidence such as screenshots etc\\>")

class port:
    def __init__(self,portNum,service,version,state):
                 self.portNum = portNum
                 self.service = service
                 self.version = version
                 self.state = state
def parseXML():
    if not os.path.exists("nmap/scan.xml"):
        print("[ERROR] scan.xml not found\nexiting")
        sys.exit(1)
    portList = []
    tree = ET.parse("nmap/scan.xml")
    root = tree.getroot()
    i = 0
    for portsFound in root.findall(".//port"):
        portnum = portsFound.get("portid")
        portProto= portsFound.get("protocol")
        for serviceFound in portsFound.findall(".//service"):
            serviceName = serviceFound.get("name")
            serviceProduct = serviceFound.get("product")
            serviceVersion = serviceFound.get("version")
        for state in portsFound.findall(".//state"):
            portstate = state.get("state")
        portnumber = str(portnum) + "/" + str(portProto)
        service = str(serviceName)
        version = str(serviceProduct) + " " + str(serviceVersion)
        portstate = str(portstate)
        portList.append(port(portnumber,service,version,portstate))
    return portList

def httpCheck(IP,portList):
    port = ""
    for i in portList:
        if i.service == "http":
            port = i.portNum
            port = port.split("/")
            results = subprocess.run(["curl", "http://"+IP+":"+port[0]], capture_output=True,text=True)
            results = results.stdout
            print("http on port " + port[0] + " contained the following comments:\n")
            for line in results.splitlines():
                if "<!--" in line:
                    print(line)
            results = subprocess.run(["curl", "http://"+IP+":"+port[0]+"/robots.txt"], capture_output=True,text=True,timeout=10)
            results1 = subprocess.run(["curl", "http://"+IP+":"+port[0]+"/ThisShouldNeverExistBecauseImadeItUpMyself"], capture_output=True, text=True, timeout=10)
            mismatch = 0
            if results1.returncode == 0 and results1.stdout:
                custom404Check = results1.stdout
            if results.returncode == 0 and results.stdout:
                content = results.stdout
            contentLines = content.split("\n")
            custom404Check= custom404Check.split("\n")
            for i in range(len(custom404Check)):
                try: 
                    test = contentLines[i]
                except:
                    test ="yea though I walk through the valley of the shadow of death I shall fear no evil"
                if test == custom404Check[i]:
                    mismatch += 1 
            if mismatch < 3:
                print(content)
            else:
                print("no Robots.txt file detected for http port "+port[0])

        if i.service == "https":
            port = i.portNum
            port = port.split("/")
            results = subprocess.run(['curl', "https://"+IP+":"+port[0]], capture_output=True,text=True)
            results = results.stdout
            print("https on port "+port[0]+" contained the following comments:\n")
            for line in results.splitlines():
                if "<!--" in line:
                    print(line)
            results = subprocess.run(["curl", "https://"+IP+":"+port[0]+"/robots.txt"], capture_output=True,text=True,timeout=10)
            results1 = subprocess.run(["curl", "https://"+IP+":"+port[0]+"/ThisShouldNeverExistBecauseImadeItUpMyself"], capture_output=True, text=True, timeout=10)
            mismatch = 0
            if results1.returncode == 0 and results1.stdout:
                custom404Check = results1.stdout
            if results.returncode == 0 and results.stdout:
                content = results.stdout
            contentLines = content.split("\n")
            custom404Check= custom404Check.split("\n")
            for i in range(len(custom404Check)):
                try: 
                    test = contentLines[i]
                except:
                    test ="yea though I walk through the valley of the shadow of death I shall fear no evil"
                if test == custom404Check[i]:
                    mismatch += 1 
            if mismatch < 3:
                print(content)
            else:
                print("no Robots.txt file detected for https port "+port[0])

def main():
    dateObj = date.today()
    currentDate = dateObj.strftime("%Y-%m-%d")
    print(currentDate)
    IP = sys.argv[1]
    scan(IP)
    print("\n\n")
    portList = parseXML()
    generateReport(currentDate,IP,portList)
    httpCheck(IP,portList)

if __name__ == "__main__":
    main()

