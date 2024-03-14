#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_practica.cdk_practica_stack import CdkPracticaStack


app = cdk.App()
CdkPracticaStack(app, "CdkPracticaStack")

app.synth()
