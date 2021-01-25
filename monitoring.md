# Designing for scalability with Erlang/OTP


## Monitoring and Preemptive Support

- your secret sauce to high availability is achieving a high level of
visibility into what is going on in your system and the ability to act on the information you collect
- will use all this information for two purposes: preemptive support
and postmortem debugging.
- Monitoring the system will allow them to pick up
early warning signs and address problems before they get out of control
- If you do not have snapshots of the system, debugging will be not be methodical and you will have to rely on guesswork
- Ensuring you have the visibility and historical data will be time well spent prior to launch

## Monitoring

- Without proper visibility in place, you can only guess the current state of
your system and are unable to spot trends and address issues before they escalate
- What thing cause the crash?
- systems need to be monitored, and information
stored for later access.

Usages:
    - Logs: record state changes in your program
    - Metrics: Polling a value at a particular point in time
    - Alarms: Event associated with a state

### Monitoring + Configuration + Management = Operation, Administration and Maintennance OAM

- All systems should let you inspect, manage, and do basic troubleshooting
- This OAM functionality have his own node
- OAM nodes can be used to handle both Erlang and non-Erlang components of your
software.
- monitor and manage your network, switches, load balancers, firewalls, hardware, OS, and stack

### Logs

- A log is an entry in a file or database that records an event that can be used as part of an audit trail
- variety of purposes, including tracing, debugging, auditing, compliance monitoring, and billing.
- have logs that allow those using them to uniquely follow the flow of
requests across nodes in order to locate issues or gather required data
- SASL logs for OTP
- If you want high availability, you need to automate the discovery of the SASL crash and error reports, and then ensure any faults get addressed.
- Think about what will give the maintainers, support engineers, DevOps
team, accountants, auditors, marketing, and customer service representatives a good overview of what is happening or has happened. Every time a notable change in state occurs, log useful information that was not previously stored
- Replaying the state transitions in the FSM would allow DevOps engineers to
retrace the steps taken by users adding items to their shopping baskets and paying for them.
- As a minimum requirement, always log the incoming and outgoing requests and results where appropriate so you are later able to identify the problematic system or component.
- Always log all Erlang shell commands and interactions
- Other items to log could include network connectivity and memory issues, which are notifications arising from the system_monitor
- “a database is a cache of your event logs,” if your database (or state) gets corrupted, the logs should tell you why

## Metrics

-  Metrics are sets of numeric data collected at regular intervals and organized in chronological order.
-  You need to retrieve data on the OS and network layers, on the middleware layer
- Improve the performance and reliability of the system and troubleshoot issues after they have occurred
- monitor the system to detect abnormal behavior and prevent failures
- predict trends and usage spikes, using the results to optimize hardware costs
- study long-term user trends and user experience
- make sure the system load doesn’t exceed available resources, requesting metrics on the memory usage of the Erlang VM.
- One typical value is an amount, a discrete or continuous value with incremental and decremental capabilities. 
- A common form of amount is counters, as we have seen.
- Gauges are a form of counter that provide a value at a particular point in time.

Measures:
    - Memory
    - Time (latency) for generate histograms

1. Amount
    - Counters
2. Gauges 
    - Memory management  
    - Histograms
3. Meters
    - Spiral
    
### Alarms

- Alarms are a subset of events associated with a state.
- While an event will tell you that something happened, an alarm will indicate that something is ongoing.
- An alarm is raised when the issue you are monitoring manifests itself.
- The alarm is said to remain active until the issue is resolved
- Alarms can also be associated with a severity. Severities include cleared, indeterminate, critical, major, minor, and warning.
- Alarms can originate from the affected node or in the OAM node itself. They can be based on thresholds or state changes, or a mixture of the two.
- In threshold-based alarms, metrics are monitored and the alarm is raised if a limit is exceeded in one of the metrics.

### Preemptive Support

- Support automation is the building of a knowledge base that is used to reduce service disruption by reacting to external stimuli and resolving problems before they escalate.
- downtime is something you need to plan for when designing your system.
- Automation is achieved through the collection and analysis of metrics, events, alarms, and configuration data.
- preemptively trying to resolve the problem before it occurs.

Keep in mind
1. Proactive support automation is focused on reducing downtime using ent to end health checks and diagnostic procedures
2. Preemptive support automation gathers data as metrics, events, alarms and logs and use the results to predict service disruptions before they occur
3. Self support automation describes the tools and libraries that can be used to troubleshoot solutions and to diagnose and resolve problems

 Conclusion:

1. Split up your system’s functionality into manageable, standalone nodes.
2. Choose a distributed architectural pattern.
3. Choose the network protocols your nodes, node families, and clusters will use when
communicating with each other.
4. Define your node interfaces, state, and data model.
5. For every interface function in your nodes, pick a retry strategy.
6. For all your data and state, pick your sharing strategy across node families, clusters,
and types, taking into consideration the needs of your retry strategy.
7. Design your system blueprint, looking at node ratios for scaling up and down.
8. Identify where to apply backpressure and load regulation.
9. Define your OAM approach, defining system and business alarms, logs, and metrics.
10. Identify where to apply support automation.
