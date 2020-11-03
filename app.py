#!/usr/bin/env python3

from aws_cdk import core

from init.init_stack import InitStack




app = core.App()
InitStack(app, "init")

app.synth()
