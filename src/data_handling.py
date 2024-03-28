{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import json\n",
    "\n",
    "data_path = os.path.join(\"data\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['timeOnIce', 'assists', 'goals', 'shots', 'hits', 'powerPlayGoals', 'powerPlayAssists', 'penaltyMinutes', 'faceOffPct', 'faceOffWins', 'faceoffTaken', 'takeaways', 'giveaways', 'shortHandedGoals', 'shortHandedAssists', 'blocked', 'plusMinus', 'evenTimeOnIce', 'powerPlayTimeOnIce', 'shortHandedTimeOnIce'])\n",
      "away team stats:\n",
      "{'shots', 'hits', 'powerPlayPercentage', 'goals', 'takeaways', 'blocked', 'powerPlayGoals', 'giveaways', 'powerPlayOpportunities', 'pim', 'faceOffWinPercentage'}\n",
      "{'shots', 'hits', 'powerPlayPercentage', 'goals', 'takeaways', 'blocked', 'powerPlayGoals', 'giveaways', 'powerPlayOpportunities', 'pim', 'faceOffWinPercentage'}\n",
      "home team stats:\n",
      "{'shots', 'hits', 'powerPlayPercentage', 'goals', 'takeaways', 'blocked', 'powerPlayGoals', 'giveaways', 'powerPlayOpportunities', 'pim', 'faceOffWinPercentage'}\n",
      "{'shots', 'hits', 'powerPlayPercentage', 'goals', 'takeaways', 'blocked', 'powerPlayGoals', 'giveaways', 'powerPlayOpportunities', 'pim', 'faceOffWinPercentage'}\n"
     ]
    }
   ],
   "source": [
    "detail = \"boxscore\"\n",
    "game_id = \"2020020001\"\n",
    "file_path = os.path.join(data_path, detail, game_id) + \".json\"\n",
    "with open(file_path) as f:\n",
    "    data = json.load(f)\n",
    "    print(data[\"teams\"][\"away\"][\"players\"][\"ID8471215\"][\"stats\"][\"skaterStats\"].keys())\n",
    "    for side in (\"away\",\"home\"):\n",
    "        print(side, \"team stats:\")\n",
    "        stats = data[\"teams\"][side][\"teamStats\"][\"teamSkaterStats\"]\n",
    "        stats_names = set(stats.keys())\n",
    "        print(stats_names)\n",
    "        stats_names.add(\"hits\")\n",
    "        print(stats_names)\n",
    "        \n",
    "        \n",
    "        # for name, value in stats.items():\n",
    "        #     print(name, value)\n",
    "\n",
    "        # print(data[\"teams\"][side][\"teamStats\"][\"teamSkaterStats\"])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "NHL_env",
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
   "version": "3.10.12"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
