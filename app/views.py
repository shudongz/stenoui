from subprocess import call
from flask import render_template, flash, redirect, url_for, request, send_from_directory
from app import app
from .forms import *

@app.route('/', methods=['GET', 'POST'])
@app.route('/query', methods=['GET', 'POST'])
def query():
    form = QueryForm()
    if request.method == 'POST':
        query = ''
        start = form.start.data
        if start:
            query = 'after ' + start.strftime("%Y-%m-%dT%H:%M:%SZ")
        end = form.end.data
        if end:
            if query:
                query += ' and '
            query += 'before ' + end.strftime("%Y-%m-%dT%H:%M:%SZ")
        if form.host.data:
            if query:
                query += ' and '
            query += 'host ' + form.host.data
        if form.net.data:
            if query:
                query += ' and '
            query += 'net ' + form.net.data
        if form.ipproto.data:
            if query:
                query += ' and '
            query += 'ip proto ' + str(form.ipproto.data)
        if form.port.data:
            if query:
                query += ' and '
            query += 'port ' + str(form.port.data)
        flash('Query: ' + query)
        cmd = [ 'stenoread', query, '-w', '/tmp/output.pcap' ]
        call(cmd)
        return redirect(url_for('download'))
    return render_template('query.html',
                           form=form
                           )

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        return send_from_directory('/tmp', 'output.pcap')
    form = Download()
    return render_template('download.html',
                           form=form,
                           output='/tmp/output.pcap'
                           )
