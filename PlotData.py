from sys import argv
import sys
import pylab
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import json

tempFile = open('database.mplot').read()
master = json.loads(tempFile)

def getListPlots():
	names = sorted(master)
	string = ''
	count = 0
	for name in names:
		string += "   " + name
		count += 1
		if count % 7 == 0:
			string += '\n'
	print string


def getData(plotName):
	return master[plotName][:-1]

def getBlank(plotName):
	return master[plotName][len(master[plotName]) - 1]

def main():
	print "Lets generate plots!"
	print "Here are plots you can choose from:"
	getListPlots()

	plotList = []

	print "Please enter the names of the plots you would like to graph together. Use a . to finish."
	print "Or type \"All [keyword]\" to graph all plots with keyword. Put a space after Strain Name."

	count = 1
	while True:
		response = raw_input(str(count) + ': ')
		if response is '.':
			break
		if response.split(" ")[0] == "All":
			allPlots = sorted(master)
			keyword = response.split(" ")[1]

			for name in allPlots:
				if keyword in name:
					plotList.append(name)
			break

		if master.has_key(response):
			plotList.append(response)
			count += 1
		else:
			print "Invalid plot name!"

	errorBars = False

	response = raw_input("Plot Error Bars? y/n: ")

	if response == 'y':
		errorBars = True

	print "Plotting " + str(len(plotList)) + " plots together."


	title = raw_input('Name your plot: ')

	plt.title(title)
	plt.xlabel('Time (hours)')
	plt.ylabel('OD')

	numPoints = len(getBlank(plotList[0]))

	plt.axis([0, 71, 0, 1.0])

	for plotname in plotList:
		dataset = getData(plotname)
		blank = getBlank(plotname)
		numPoints = len(blank)

		meanArray = np.array([0.0] * numPoints)

		for data in dataset:
			meanArray = meanArray + np.array(data)
		meanArray = meanArray / float(len(dataset))
		meanArray = meanArray - np.array(blank)

		deviation = [0.0] * numPoints

		for i in range(numPoints):
			calcArray = []

			for data in dataset:
				calcArray.append(data[i])
			calcArray = np.array(calcArray)

			deviation[i] = np.std(calcArray)

		xAxis = np.arange(0, numPoints, 1)

		error = [deviation, deviation]

		if errorBars:
			plt.errorbar(xAxis, meanArray, yerr=error, label=plotname)
		else:
			plt.errorbar(xAxis, meanArray, label=plotname)

	path = glob.glob(os.path.dirname(os.path.abspath(__file__)))[0]
	path = path + '/plots/'
	if not os.path.exists(path):
		os.makedirs(path)

	plt.legend(fontsize=8, loc=2)
	pylab.savefig(path + title + '.png')
	plt.clf()


main()




