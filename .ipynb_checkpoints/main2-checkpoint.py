{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "001887f2",
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
   "execution_count": null,
   "id": "77c0f7d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# read csv data and load to budgetDB\n",
    "csvpath = os.path.join(\"Resources\",\"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2da0e1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# creat a txt file to hold the analysis\n",
    "outputfile = os.path.join(\"Analysis\",\"budget_analysis.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f3c0fd89",
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
   "execution_count": null,
   "id": "4f807576",
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
   "execution_count": null,
   "id": "ad264653",
   "metadata": {},
   "outputs": [],
   "source": [
    "# use csvreader object to import the csv library with csvreader object\n",
    "with open(csvpath, newline = \"\") as csvfile:\n",
    "#    # create a csv reader object\n",
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
   "execution_count": null,
   "id": "27fc81c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "for p in csvreader:\n",
    "    print(\"date: \" + p[0])\n",
    "    print(\"profit: \" + p[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83749f03",
   "metadata": {},
   "outputs": [],
   "source": [
    "# read the header row\n",
    "header = next(csvreader)\n",
    "print(f\"csv header:{header}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b441a20",
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
   "id": "a815e200",
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
   "id": "6bf35c14",
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
