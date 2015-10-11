#!/usr/bin/env python

import andle.android
import andle.sdk


def update(path, dryrun=False, remote=False):
	"""
	update android projects config
	:param path: projects path
	:param dryrun: dryrun or not
	"""
	data = sdk.load()
	android.update(path, data, dryrun, remote)


def setsdk(path):
	"""
	set android sdk path
	:param path: sdk path
	"""
	sdk.setpath(path)
