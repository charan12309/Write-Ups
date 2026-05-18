# Introduction to the penetration tester path

## Introduction to the penetration tester path

Penetration testing follows a repeatable lifecycle. Each phase builds on the last.

```
Pre-engagement
  -> Information gathering
  -> Vulnerability assessment
  -> Exploitation
  -> Post-exploitation
  -> Lateral movement
  -> Proof of concept
  -> Post-engagement
```

### Lifecycle overview

1. **Pre-engagement** — define scope, rules, targets, and contracts.
2. **Information gathering** — collect intelligence and map the attack surface.
3. **Vulnerability assessment** — identify weaknesses worth testing.
4. **Exploitation** — validate weaknesses through controlled attacks.
5. **Post-exploitation** — escalate privileges and deepen access.
6. **Lateral movement** — pivot to additional systems and segments.
7. **Proof of concept** — document impact and reproducibility.
8. **Post-engagement** — clean up, report, and retest if needed.

### Exploitation focus areas

Exploitation usually splits into two tracks:

* **Network services** — find exposed services, weak configs, and outdated software.
* **Web applications** — find application flaws and insecure business logic.

### Risk management

Risk management means finding risk, rating it, and reducing it.

#### Common risk responses

| Response | Meaning                          | Typical use                             |
| -------- | -------------------------------- | --------------------------------------- |
| Accept   | Live with the risk.              | Low impact and low likelihood.          |
| Transfer | Shift the risk to another party. | Insurance or managed services.          |
| Avoid    | Stop the risky activity.         | Risk is too high to justify.            |
| Mitigate | Reduce likelihood or impact.     | Add controls, hardening, or monitoring. |

### What a pentester does

#### Core responsibilities

* Find vulnerabilities.
* Document them clearly.
* Show how to reproduce them.
* Recommend realistic fixes.

#### Out of scope

* Fix the vulnerabilities.
* Apply patches.
* Rewrite the client's code.
* Monitor systems long term.

### Vulnerability assessment vs. penetration test

| Topic         | Vulnerability assessment       | Penetration test                            |
| ------------- | ------------------------------ | ------------------------------------------- |
| Method        | Mostly automated scanning      | Automated plus manual testing               |
| Strength      | Fast coverage of known issues  | Finds chained and custom issues             |
| Weakness      | Misses context and logic flaws | Takes more time and skill                   |
| Output        | List of potential findings     | Validated findings with impact              |
| Typical tools | Nessus, OpenVAS                | Scanners, manual testing, custom tradecraft |

### External vs. internal pentest

| Type     | Starting position          | Typical targets                                      | Goal                              |
| -------- | -------------------------- | ---------------------------------------------------- | --------------------------------- |
| External | Outside the company        | Public websites, VPNs, mail servers, APIs            | Break through the perimeter       |
| Internal | Inside the company network | AD, file shares, databases, endpoints, internal apps | Measure blast radius after access |

In practice, the flow often looks like this:

1. Run an external test.
2. Gain internal access.
3. Run an internal test from the new foothold.

### Types of penetration testing

| Type        | What you know                       | Notes                                    |
| ----------- | ----------------------------------- | ---------------------------------------- |
| Black box   | Almost nothing                      | Most realistic. Usually hardest.         |
| Grey box    | Partial knowledge                   | Common in real engagements.              |
| White box   | Full knowledge                      | Fastest and deepest coverage.            |
| Red team    | Full attack simulation              | May include phishing or physical access. |
| Purple team | Attackers and defenders collaborate | Improves detection and response.         |

#### Real-world mapping

* **Bug bounty** — usually black box.
* **Most client pentests** — usually grey box.
* **Code audit** — usually white box.
* **Advanced simulation** — often red team.

### Common testing environments

* **Network** — routers, switches, and core infrastructure.
* **Web applications** — websites and portals.
* **Mobile** — Android and iOS apps.
* **API** — backend services and endpoints.
* **Thick clients** — desktop applications.
* **IoT** — cameras, sensors, and smart devices.
* **Cloud** — AWS, Azure, and GCP.
* **Source code** — secure code review.
* **Physical** — locks, badges, and server rooms.
* **Employees** — phishing and social engineering.
* **Hosts and servers** — workstations and servers.
* **Firewalls and IDS** — security device misconfigurations.

### Password spraying

Password spraying tests one password against many usernames. The goal is one valid login without triggering account lockouts.

```
User A --\
User B ----> Try [Winter2026!] --> Find one valid login
User C --/
```

> Password spraying lowers lockout risk, but it creates a longer detection window.

### Information gathering structure

#### 1. OSINT

Collect public information before touching the target.

* Search Google, GitHub, LinkedIn, and DNS data.
* Look for leaked credentials, subdomains, and employee details.

#### 2. Infrastructure enumeration

Map the external footprint.

* Identify DNS servers, mail servers, web servers, and cloud assets.
* Build a view of the full attack surface.

#### 3. Service enumeration

Profile each discovered service.

* Identify protocols such as FTP, SSH, HTTP, SMB, and RDP.
* Record versions and exposed functionality.
* Flag outdated software and weak configurations.

#### 4. Host enumeration

Profile each system in context.

* Identify the operating system.
* List open ports and listening services.
* Determine the host's role and peer relationships.

#### 5. Pillaging

Pillaging starts after access. Pull useful data from the compromised host.

* Passwords in config files.
* SSH keys and tokens.
* Employee data and internal documents.
* Scripts with hardcoded credentials.

### Vulnerability assessment lenses

| Lens         | Core question                    |
| ------------ | -------------------------------- |
| Descriptive  | What do I see?                   |
| Diagnostic   | Why does it exist?               |
| Predictive   | What happens if it is exploited? |
| Prescriptive | What should change?              |

### Exploitation

Before exploitation, score each option against three factors:

1. **Probability of success** — how likely the attack is to work.
2. **Complexity** — how hard the attack is to execute.
3. **Probability of damage** — how likely the attack is to disrupt the target.

#### Prioritization rule

* **High success + low complexity + low damage** — test first.
* **Low success + high complexity + high damage** — avoid or leave for last.

#### Safe validation workflow

If no public proof of concept works immediately:

1. Build a VM that mirrors the target.
2. Match the OS and service versions.
3. Test locally first.
4. Confirm the exploit works safely.
5. Use it on the real target only after validation.

> If an attack might cause damage, ask the client first. Never guess on production systems.

### Post-exploitation

Post-exploitation is noisier than initial access. Detection risk goes up fast.

#### Evasive testing modes

| Mode        | Behavior                               |
| ----------- | -------------------------------------- |
| Evasive     | Stay hidden as long as possible.       |
| Non-evasive | Ignore detection risk.                 |
| Hybrid      | Start quietly, then increase pressure. |

#### Internal information gathering

Once inside, you see the network differently.

Look for:

* Local network structure.
* Connected machines and trust relationships.
* File shares, printers, and databases.
* Routing paths and management channels.

#### Pillaging targets

Useful data often includes:

* Passwords in config files.
* SSH keys and saved credentials.
* Documents with sensitive data.
* Emails and chat exports.
* VPN configs and routing data.
* ARP tables and interface data.

#### Persistence

Persistence keeps access alive after the initial foothold breaks.

* If the exploit path dies, you still need re-entry.
* Persistence often comes early for that reason.

> Persistence mechanisms can create operational risk. Only use them within scope and approval.

#### Privilege escalation

Initial access rarely gives full control.

| Platform | Typical goal                                   |
| -------- | ---------------------------------------------- |
| Linux    | `root`                                         |
| Windows  | `SYSTEM` or domain-level administrative access |

Common paths:

* Exploit a local vulnerability.
* Recover stored credentials from a higher-privilege user.

#### Data exfiltration

Data exfiltration tests whether sensitive data can leave the environment.

* DLP and EDR may detect or block the transfer.
* Use fake data when possible.
* Capture screenshots or recordings as evidence.

> Always get client approval before exfiltrating any data. Prefer fake test data over real sensitive data.

#### Full post-exploitation flow

```
Get access
  -> Establish persistence
  -> Gather internal information
  -> Pillage useful data
  -> Assess internal weaknesses
  -> Escalate privileges
  -> Exfiltrate approved test data
  -> Move laterally
```

### Lateral movement

Lateral movement expands one compromise into a wider compromise.

Attackers do not stop at one host. They pivot, reuse credentials, and chain trust relationships until they reach critical systems.

#### Common steps

1. **Pivoting** — use one compromised host to reach another.
2. **Evasion** — avoid IPS, IDS, EDR, and blue team visibility.
3. **Internal discovery** — map reachable systems and services.
4. **Internal assessment** — find weak configs and trust abuse paths.
5. **Internal exploitation** — crack passwords or reuse credentials.
6. **Repeat** — perform post-exploitation again on each new host.

#### Key techniques

* **Pass-the-Hash** — authenticate with a stolen password hash.
* **Responder** — capture NTLMv2 authentication attempts for relay or cracking workflows.

#### Example attack chain

```
Compromised web server
  -> Pivot to internal network
  -> Reach database server
  -> Reuse or crack credentials
  -> Discover domain admin material
  -> Compromise Active Directory
```

### Proof of concept

A proof of concept shows that the vulnerability is real and reproducible.

#### Good PoC output

* Step-by-step evidence.
* Commands, screenshots, or logs.
* Clear impact.
* Clear remediation.

#### What to avoid

Do not ship only a one-off exploit script.

If defenders patch only against your script, the root issue stays open.

#### Focus on root cause

| Scenario                        | Weak fix                | Correct fix                             |
| ------------------------------- | ----------------------- | --------------------------------------- |
| Domain admin uses `Password123` | Reset that one password | Fix password policy and account hygiene |

Include:

* The full attack chain.
* The root cause of each finding.
* Remediation that breaks the chain permanently.

### Post-engagement

#### 1. Cleanup

* Remove tools and artifacts.
* Revert authorized changes.
* Record what changed.

#### 2. Draft report

Include:

* Executive summary.
* Attack chain.
* Findings with risk ratings.
* Reproduction steps.
* Supporting appendices.

#### 3. Report review meeting

* Walk the client through the findings.
* Answer open questions.
* Clarify business impact.

#### 4. Final report

* Incorporate client feedback.
* Publish the final version.

#### 5. Post-remediation testing

* Retest fixed findings.
* Confirm whether each issue is resolved.
* Deliver a remediation validation report.

#### 6. Data retention

* Keep client data encrypted.
* Retain it only as long as needed.
* Wipe it when the engagement closes.

#### 7. Closeout

* Wipe remaining data and systems.
* Complete invoicing.
* Send final follow-up if required.
