{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5ddbad81",
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
   "execution_count": 2,
   "id": "0f3c390f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# read csv data and load to budgetDB\n",
    "csvpath = os.path.join(\"Resources\",\"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "de9f85fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# creat a txt file to hold the analysis\n",
    "outputfile = os.path.join(\"Analysis\",\"budget_analysis.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b98a7e27",
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
   "execution_count": 5,
   "id": "a0ffac63",
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
   "execution_count": 6,
   "id": "5234956f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_csv.reader object at 0x000001E62A5A21C0>\n"
     ]
    }
   ],
   "source": [
    "# use csvreader object to read the csv library\n",
    "with open(csvpath, \"r\",newline = \"\") as csvfile:\n",
    "    # create a csv reader object\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    # skip the first row since it has all of the column information\n",
    "    #next(csvreader)\n",
    "    \n",
    "#header: date, profit/losses\n",
    "print(csvreader)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "25d7780e",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-e6fefb3ef218>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# read the header row\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mheader\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnext\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcsvreader\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mf\"csv header:{header}\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "# read the header row\n",
    "header = next(csvreader)\n",
    "print(f\"csv header:{header}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4c225dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "for row in csvreader:\n",
    "    print(f\"{row[0]}\")\n",
    "#    for item in row:      \n",
    "#    print(item)\n",
    "#    print(\"-----\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f6e411c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# move to the next row (first row)\n",
    "firstRow = next(csvreader)\n",
    "totalMonths = (len(f\"[csvfile.index(months)][csvfile]\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "581c0d75",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(header)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5dee213",
   "metadata": {},
   "outputs": [],
   "source": [
    "output = (\n",
    "    f\"Financial Anaylsis \\n\"\n",
    "    f\"------------------------- \\n\"\n",
    "    f\"Total Months: {totalMonths} \\n\")\n",
    "print(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ab3a15e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# establish the previous budget and note that budget is in index 1\n",
    "previousBudget = float(firstRow[1])\n",
    "previousBudget = float(firstRow[1])\n",
    "#print(previousBudget)\n",
    "# increment the total months and add on to the total amount of budget\n",
    "totalMonths += 1\n",
    "totalBudget += float(firstRow[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad07881d",
   "metadata": {},
   "outputs": [],
   "source": [
    "    for months in csvreader:\n",
    "        print(months)\n",
    "        #f\"({months+1}){months}\")\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f372d9d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "        totalMonths += 1\n",
    "\n",
    "        totalBudget += float(row[1])\n",
    "\n",
    "        # calculate the net change\n",
    "        netChange = float(row[1]) - previousBudget\n",
    "        # add on to the list of monthly changes\n",
    "        monthChange.append(netChange)\n",
    "\n",
    "\n",
    "        # add the first month that a change occurred, note that the month is in index 0\n",
    "        months.append(row[0])\n",
    "\n",
    "\n",
    "        # update the previous budget\n",
    "        previousBudget = float(row[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9404d30",
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate the average change \n",
    "averageChange = sum(monthChange) / len(monthChange)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebfec924",
   "metadata": {},
   "outputs": [],
   "source": [
    "# set variables to hold the month and value of the greatest increase and decrease in profits\n",
    "greatestIncrease = [months[0], monthChange[0]]\n",
    "greatestDecrease = [months[0], monthChange[0]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7da7fce1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# create loop to calculate the index of the greatest and least monthly change\n",
    "for m in range(len(monthChange)):\n",
    "    if (monthChange[m] > greatestIncrease[1]):\n",
    "        greatestIncrease[1] = monthChange[m]\n",
    "        greatestIncrease[0] = months[m]\n",
    "\n",
    "\n",
    "    if (monthChange[m] < greatestDecrease[1]):\n",
    "        greatestDecrease[1] = monthChange[m]\n",
    "        greatestDecrease[0] = months[m]    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b134522",
   "metadata": {},
   "outputs": [],
   "source": [
    "# start generating the output\n",
    "output = (\n",
    "    f\"Financial Anaylsis \\n\"\n",
    "    f\"------------------------- \\n\"\n",
    "    f\"Total Months: {totalMonths} \\n\"\n",
    "    f\"Total Budget: ${totalBudget} \\n\"\n",
    "    f\"Average Change: ${averageChange} \\n\"\n",
    "    f\"Greatest Increase in Profit: {greatestIncrease[0]} ({greatestIncrease[1]}) \\n\"\n",
    "    f\"Greatest Dncrease in Profit: {greatestDecrease[0]} ({greatestDecrease[1]})\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc27fa13",
   "metadata": {},
   "outputs": [],
   "source": [
    "# print the output\n",
    "print(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb74b115",
   "metadata": {},
   "outputs": [],
   "source": [
    "# export the output to the output text file\n",
    "with open(outputfile, \"w\") as textfile:\n",
    "    textfile.write(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93f380ab",
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
