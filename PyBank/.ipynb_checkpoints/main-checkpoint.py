{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7c7c836b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import os modules to create path across operating system to load csv file\n",
    "import os\n",
    "# module for reading csv files\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d33c6089",
   "metadata": {},
   "outputs": [],
   "source": [
    "# read csv data and load to budgetDB  csvpath=>inputfile\n",
    "inputfile = os.path.join(\"Resources\",\"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e9388053",
   "metadata": {},
   "outputs": [],
   "source": [
    "# creat a txt file to hold the analysis\n",
    "outputfile = os.path.join(\"Analysis\",\"budget_analysis.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6a7f1de4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# set var and initialize to zero\n",
    "totalMonths = 0     \n",
    "totalBudget = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d698070e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# set list to store all of the monthly changes\n",
    "monthChange = []      \n",
    "months = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8cd4227e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# use csvreader object to read the csv file with csvreader object,with open(csvpath, newline = \"\") as csvfile:\n",
    "#with open(csvpath) as csvfile:\n",
    "    # create a csv reader object\n",
    "#    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    # skip the first row since it has all of the column information\n",
    "    #next(csvreader)\n",
    "    \n",
    "#header: date, profit/losses\n",
    "#print(csvreader)\n",
    "\n",
    "\n",
    "#with open(inputfile) as budget_data:\n",
    "#    # create a csv reader object\n",
    "#    csvreader = csv.reader(budget_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "18eb39dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#with open(cereal_csv, encoding='utf-8-sig') as csvfile:\n",
    "#    csv_reader = csv.reader(csvfile, delimiter=\",\")\n",
    "\n",
    "    # @NOTE: This time, we do not use `next(csv_reader)` because there is no header for this file\n",
    "\n",
    "    # read the header row\n",
    "#    header = next(csvreader)\n",
    "    # move to the next row (first row)\n",
    "#firstRow = next(csvreader)\n",
    "#print(firstRow)\n",
    "\n",
    "#    # Read through each row of data after the header\n",
    "#    for row in csv_reader:\n",
    "\n",
    "#        # Convert row to float and compare to grams of fiber\n",
    " #       if float(row[7]) >= 5:\n",
    " #           print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "702d7614",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Jan-2010', '867884']\n",
      "<_csv.reader object at 0x0000028BABC2A700>\n"
     ]
    }
   ],
   "source": [
    "with open(inputfile) as budget_data:\n",
    "    # create a csv reader object\n",
    "    csvreader = csv.reader(budget_data)\n",
    "\n",
    "\n",
    "    # read the header row\n",
    "    header = next(csvreader)\n",
    "    # move to the next row (first row)\n",
    "    firstRow = next(csvreader)\n",
    "    \n",
    "    print(firstRow)\n",
    "    print(csvreader)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f4585842",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 867884.0\n"
     ]
    }
   ],
   "source": [
    "# establish the previous budget and note that budget is in index 1\n",
    "previousBudget = float(firstRow[1])\n",
    "# increment the total months and add on to the total amount of budget\n",
    "totalMonths += 1\n",
    "totalBudget += float(firstRow[1])\n",
    "\n",
    "print(totalMonths, totalBudget)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4067d2fa",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-10-ae6affe81ac7>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mcsvreader\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m     \u001b[0mtotalMonths\u001b[0m \u001b[1;33m+=\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mtotalBudget\u001b[0m \u001b[1;33m+=\u001b[0m \u001b[0mfloat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "for row in csvreader:\n",
    "    totalMonths += 1\n",
    "    \n",
    "    totalBudget += float(row[1])\n",
    "\n",
    "# calculate the net change\n",
    "netChange = float(row[1]) - previousBudget\n",
    "\n",
    "# add on to the list of monthly changes\n",
    "monthlyChanges.append(netChange)\n",
    "\n",
    "# add the first month that a change occurred, note that the month is in index 0\n",
    " months.append(row[0])\n",
    "    \n",
    "# update the previous budget\n",
    "previousBudget = float(row[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0747e5f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate the average change \n",
    "averageChange = sum(monthlyChanges) / len(monthlyChanges)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab0f0f2c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# set variables to hold the month and value of the greatest increase and decrease in profits\n",
    "greatestIncrease = [months[0], monthlyChanges[0]]\n",
    "greatestDecrease = [months[0], monthlyChanges[0]]\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac6a35ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "# create loop to calculate the index of the greatest and least monthly change\n",
    "for m in range(len(monthlyChanges)):\n",
    "    if (monthlyChanges[m] > greatestIncrease[1]):\n",
    "        greatestIncrease[1] = monthlyChanges[m]\n",
    "        greatestIncrease[0] = months[m]\n",
    "\n",
    "\n",
    "    if (monthlyChanges[m] < greatestDecrease[1]):\n",
    "        greatestDecrease[1] = monthlyChanges[m]\n",
    "        greatestDecrease[0] = months[m]    \n",
    "\n",
    "\n",
    "# start generating the output\n",
    "output = (\n",
    "    f\"Financial Anaylsis \\n\"\n",
    "    f\"------------------------- \\n\"\n",
    "    f\"Total Months: {totalMonths} \\n\"\n",
    "    f\"Total Budget: ${totalBudget} \\n\"\n",
    "    f\"Average Change: ${averageChange} \\n\"\n",
    "    f\"Greatest Increase in Profit: {greatestIncrease[0]} ({greatestIncrease[1]}) \\n\"\n",
    "    f\"Greatest Dncrease in Profit: {greatestDecrease[0]} ({greatestDecrease[1]})\"\n",
    "    )\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bef5340",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# print the output\n",
    "print(output)\n",
    "\n",
    "\n",
    "# export the output to the output text file\n",
    "with open(outputfile, \"w\") as textfile:\n",
    "    textfile.write(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ac29c09",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff9f8295",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
