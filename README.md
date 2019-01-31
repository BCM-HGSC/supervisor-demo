# supervisor-demo

Simple example of a config file and job script to demonstrate the use of supervisor

Get the software.

    git clone https://github.com/BCM-HGSC/supervisor-demo.git
    cd supervisor-demo

Cleanup if re-running the demo.

    rm -f bar.log bar_p.log foo.log supervisord.log

Start everything.

    supervisord -c supervisord.conf

Using supervisorctl:

    supervisorctl -c supervisord.conf help
    supervisorctl -c supervisord.conf pid
    supervisorctl -c supervisord.conf avail
    supervisorctl -c supervisord.conf status
    supervisorctl -c supervisord.conf pid all

Looking at a single "program":

    cat bar_p.log
    supervisorctl -c supervisord.conf tail foobar:bar_p
    supervisorctl -c supervisord.conf signal ALRM foobar:bar_p
    supervisorctl -c supervisord.conf tail foobar:bar_p

Stopping and starting a single program:

    supervisorctl -c supervisord.conf stop foobar:bar
    supervisorctl -c supervisord.conf status
    supervisorctl -c supervisord.conf pid all
    supervisorctl -c supervisord.conf start foobar:bar
    supervisorctl -c supervisord.conf status
    supervisorctl -c supervisord.conf tail foobar:bar

Sending signals:

    supervisorctl -c supervisord.conf stop all
    supervisorctl -c supervisord.conf status
    supervisorctl -c supervisord.conf start foobar:foo
    supervisorctl -c supervisord.conf signal ALRM foobar:foo
    supervisorctl -c supervisord.conf signal ALRM foobar:*
    supervisorctl -c supervisord.conf tail foobar:foo
    supervisorctl -c supervisord.conf stop foobar:*
    supervisorctl -c supervisord.conf status
    supervisorctl -c supervisord.conf signal ALRM foobar:*  # does nothing

Demo shutdown when everything is running.

    supervisorctl -c supervisord.conf start foobar:*
    supervisorctl -c supervisord.conf status
    supervisorctl -c supervisord.conf shutdown
    tail *.log

