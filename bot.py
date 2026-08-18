import discord

# 1. SET UP INTENTS
intents = discord.Intents.default()
intents.message_content = True  # lets bot read what people type
intents.messages = True         

client = discord.Client(intents=intents)

# 2. ALL 128 PRESET TRIGGERS
AUTO_REPLIES = {
    "Scroll to the section Everything About Sports Betting!, locate the second and third words.": "Expert tips",
    "Scroll to the section called Changing Regulations, locate the first two words.": "Regulations can",
    "Scroll to the section called Our Mission, locate the first 2 words": "To help",
    "Scroll to the section called Professional Experts, locate the ninth and tenth words of the description.": "specialized knowledge",
    "Scroll to the section called Betting Bonuses, locate the last 2 words.": "Reload bonuses",
    "Scroll to the section called Our Mission, locate the last two words of the description.": "smarter betting.",
    "Scroll to the section called How Do We Rate Top Asian Betting Sites?, then to the sub-section Odds Comparison, and locate the last two words.": "Live betting",
    "Scroll to the section called Our Mission, locate the last two words of the first sentence.": "better choices",
    "Scroll to the section called Stay Updated About Sports Betting and locate the fourth and fifth words.": "sports predictions",
    "Scroll to the section called Data Research, locate the last 2 words": "withdrawal speed",
    "Scroll to the section called Live & In-Play Betting, locate the last two words of the first sentence.": "crypto payments",
    "Scroll to the section called Markets at the Crypto and Bitcoin Sports Betting Websites, locate the fourth and fifth words of the first sentence.": "sports markets",
    "Scroll to the section called Security & Safety in Top Crypto Betting Sites, locate the words between \"use\" and \"and\" in the Use a VPN carefully bullet.": "trusted providers",
    "Scroll to the section called Growth of Crypto Sports Betting: What Will We See in the Future?, locate the last two words of the Metaverse Betting row.": "social features",
    "Scroll to the section called Bonuses Betting Requirements in the Best Cryptocurrency Betting Sites, locate the words between \"your\" and \"and\" in the first bullet point.": "balance steady",
    "Scroll to the section called Live Betting Tools, locate the words between \"the\" and \"how\".": "odds refresh,",
    "Scroll to the section called Bonuses and Promotions, locate the last two words of the first sentence.": "careful look.",
    "Scroll to the section called Bonuses Betting Requirements in the Best Cryptocurrency Betting Sites, locate the last two words of the Avoid switching coins bullet point.": "reset progress",
    "Scroll to the section called Odds Boosts, locate the first two words.": "Alongside cashback,",
    "Scroll to the section called Football Betting Options, locate the third and fourth words of the third sentence.": "same time,",
    "Find the account description and locate the first 2 words in it.": "SmartbettingGuide is",
    "Scroll to the section called Traditional Sports Markets, locate the words between \"like\" and \"usually\".": "player props",
    "Scroll to the section called Plan for Fees and Network Speeds and locate the first two words.": "Different networks",
    "Scroll to the section called Supported Cryptocurrencies & Payment Methods, locate the first two words.": "Best crypto",
    "Scroll to the section called Odds Fairness, locate the last three words.": "keeps margins reasonable.",
    "Scroll to the section called What is Betwinner minimum deposit?, locate the first 2 words.": "Betwinner mininum",
    "Scroll to the section called Cryptocurrency Options, locate the last 2 words.": "usually irreversible.",
    "Scroll to the section called Security Features at Asian Betting Sites and locate the first two words.": "Security features",
    "Scroll to the section called Keep Stakes Consistent, locate the last 2 words.": "long-term results.",
    "Scroll to the section called How do I contact 22bet support?, locate the last 2 words.": "international support",
    "Scroll to the section called FAQ about Tennis Handicap Betting, and locate the first two words of the answer to \"How does tennis handicap betting work?\".": "Tennis handicap",
    "Scroll to the section called \"We Offer Knowledge & Education\", locate the words between \"and\" and \"help\" in the second sentence.": "Expert recommendations",
    "Scroll to the section called \"Our Achievements\", locate the words between \"of\" and \"to\" under \"Written Articles\".": "Online betting",
    "Scroll to the section called \"Bonuses & Promotions Guide at the Best Crypto Betting Sites\", locate the last two words.": "USDT deposits",
    "Find \"Welcome to Pokeriomokykla.com\" section and locate the first 2 words.": "Pokeriomokykla.com is",
    "Scroll to the section called \"How We Test & Review the Top Crypto Betting Sites\", then to the sub-section \"Security Practices\", locate the second, third, and fourth words of the last sentence.": "security practices are",
    "Scroll to the section called \"About Us\", locate the first 2 words.": "our vision",
    "Scroll to the section called \"Plan for Fees and Network Speeds\", locate the last two words of the first paragraph.": "frequent bettors.",
    "Scroll to the section called \"Esports Betting Markets\", locate the words between \"FIFA\" and \"constantly\" in the first paragraph.": "update odds",
    "Scroll to the section called \"Major Cryptocurrencies (BTC, ETH, LTC)\", locate the last two words of the second sentence.": "confirmation times.",
    "Scroll to the section called \"Honest Rating\", locate the last 2 words.": "individual needs",
    "Scroll to the section called \"Native Platform Tokens\", locate the last two words.": "faster withdrawals.",
    "Scroll to the section called \"Blockchain Payments\", locate the last two words of the description.": "clearly stated.",
    "Scroll to the section called \"Security Practices\", locate the first two words.": "strong security",
    "Scroll to the section called \"Major Cryptocurrencies (BTC, ETH, LTC)\", locate the words between \"of\" and \"or\" in the last sentence.": "small bets",
    "Scroll to the section called \"Proportional Betting\", locate the first two words.": "Proportional Betting",
    "Scroll to the section called \"Our Vision\", locate the fourth and fifth words of the description.": "most trusted",
    "Scroll to the section called \"Most Popular Sports Betting Bonuses for Crypto Bettors\", locate the second and third words of the Welcome Bonus description.": "matched crypto",
    "Scroll to the section called \"Regulation\", locate the last two words.": "Deposit limits",
    "Scroll to the section called \"How Do We Rate Top Asian Betting Sites?\", then to the sub-section \"Mobile Site & App\", and locate the last two words.": "Payment features",
    "Scroll to the section called \"Hedge With Stablecoins\", locate the sixth, seventh, and eighth words.": "Safest tools for",
    "Scroll to the section called \"Legal Status of Bitcoin and Crypto Sports Betting\", locate the last two words of the first sentence in the second paragraph.": "Grey area",
    "Scroll to the section called \"Special & Prediction Markets\", locate the words between \"results \" and \"major\".": "stock movements",
    "Scroll to the section called \"Odds Fairness\", locate the two words following \"overall\" in the last sentence.": "margin levels",
    "Scroll to the section called \"Markets at the Crypto and Bitcoin Sports Betting Websites\", then to the sub-section \"Esports Betting Markets\", and locate the first four words of the first sentence.": "eSports suits crypto bettors",
    "Scroll to the section called \"Security Features at Asian Betting Sites\" and locate the last two words.": "Bookie betting",
    "Scroll to the section called \"Traditional & Regional Sports Betting Options\", locate the first 2 words.": "Traditional sports",
    "Scroll to the section called \"Cricket Betting Options\", locate the last two words of the final paragraph.": "Team strategies",
    "Scroll to the section called \"Are Asian bookies safe?\" and locate the third and fourth words.": "Asian sports",
    "Scroll to the section called \"Local Payment Systems\", locate the first 2 words.": "Local payment",
    "Scroll to the section called \"Mobile Betting: Apps and Mobile Sites in Asia\", locate the first 2 words.": "Best online",
    "Scroll to the section called \"Event-Based Promotions\", locate the first two words.": "Many asian",
    "Scroll to the section called \"18+ Only. Play Responsibly.\" and locate the first two words of the second sentence.": "If gambling",
    "Find the section called \"Betting Ratings\", locate the third and the fourth words.": "Best betting",
    "Scroll to the section called \"Security & Safety in Top Crypto Betting Sites\", locate the fourth and fifth words of the instruction.": "Gives you",
    "Scroll to the section called \"Is Rolletto available in the UK?\", locate the fifth and sixth words.": "available for",
    "Scroll to the section called \"Most Popular Sports Betting Bonuses for Crypto Bettors\", locate the first two words.": "This overview",
    "Scroll to the section called \"Our Story\", locate the words between \"a\" and \"among\" in the description.": "small project.",
    "Scroll to the section called \"Popular Sports and Events at Best Asian Betting Sites\", locate the last two words.": "bookies online",
    "Scroll to the section called \"Asian Bookmakers: What to Expect?\", locate the words between \"and\" and \"accounts\" in the Mobile compatibility point.": "manage their",
    "Scroll to the section called \"Bonuses & Promotions at the Best Sports Betting Sites Reviewe\", locate the last two words.": "betting sites",
    "Scroll to the section called \"Stay Updated About Sports Betting\" and locate the first two words.": "Free expert",
    "Find the section called \"Let`s keep in touch\", locate the first field and copy the name of it (1 word).": "Name",
    "Scroll to the section called \"How do I create an account on Vave?\" and locate the third and fourth words.": "Create an",
    "Find the section called \"About SmartBettingGuide\", locate the first 2 words in the third sentence.": "We also",
    "Scroll to the section called \"Customer Support\", locate the last two words of the section.": "handles them.",
    "Scroll to the section called \"Bonuses Betting Requirements in the Best Cryptocurrency Betting Sites\", locate the last two words of the first sentence.": "bonus abuse.",
    "Scroll to the section called \"Responsible Gambling at the Top Crypto Betting Sites\", locate the last two words of the description in the Crypto-specific support bullet.": "these issues.",
    "Scroll to the section called \"Security & Safety in Top Crypto Betting Sites\", locate the first two words of the description in the Move larger winnings bullet.": "Hardware wallets",
    "Scroll to the section called \"Pros and Cons of Crypto Betting Sites\", then to the sub-section \"Pros\", locate the last three words of the second point.": "or card charges.",
    "Scroll to the section called \"Supported Cryptocurrencies & Payment Methods\", then to the sub-section \"Fiat On-Ramps (Card, Bank Transfer)\", locate the third and fourth words of the last sentence.": "often have",
    "Scroll to the section called \"Markets at the Crypto and Bitcoin Sports Betting Websites\", locate the words between \"of\" and \"as\".": "sports markets,",
    "Scroll to the section called \"Are crypto betting sites legal?\", and locate the third and fourth words.": "sites legality",
    "Scroll to the section called \"How We Test & Review the Top Crypto Betting Sites\", then to the sub-section \"Range of Markets\", and locate the first two words of the last sentence.": "We evaluate",
    "Scroll to the section called \"Understanding Betting Odds at Top Sites for Sports Betting\", locate the first two words.": "Betting Odds",
    "Scroll to the section called \"Fixed Betting\", locate the first two words.": "Fixed betting",
    "Scroll to the section called \"Bankroll Growth Strategy\", locate the first two words.": "Consider employing",
    "Scroll to the section called \"Interface Quality & Mobile Betting Platforms\", locate the last two words.": "betting markets.",
    "Scroll to the section called \"Top 10 Best Crypto Betting Sites by Categories\", locate the last two words of the BC.Game description.": "Loyalty Program",
    "Scroll to the section called \"Asian Betting Features\", locate the words between \"a\" and \"with\" in the Localized Emphasis point.": "deep connection",
    "Scroll to the section called \"Range of Markets\", locate the first two words.": "We first",
    "Scroll to the section called \"Odds Fairness\", locate the words between \"the\" and \"margins\" in the last sentence.": "operator keeps",
    "Scroll to the section called \"Bonuses Betting Requirements in the Best Cryptocurrency Betting Sites\", locate the last two words of the bolded phrase in the Watch the expiry timer bullet point.": "expiry timer",
    "Scroll to the section called \"Special & Prediction Markets\", locate the words between \"traditional\" and \"making\" in the second sentence.": "novelty bets,",
    "Scroll to the section called \"Security & Safety in Top Crypto Betting Sites\", locate the second and third words.": "betting sites",
    "Scroll to the section called \"Understanding Asian Betting Odds & Markets\", locate the first two words.": "Asia sports",
    "Scroll to the section called \"How Do We Rate Top Asian Betting Sites?\", then to the sub-section \"Betting Markets\", and locate the last two words.": "major competitions.",
    "Scroll to the section called \"Regulatory Compliance, Protection & Reliability\", locate the first two words.": "We support",
    "Scroll to the section called \"Fiat On-Ramps (Card, Bank Transfer)\", locate the second and third words of the last sentence.": "card purchases",
    "Scroll to the section called \"Bonuses & Promotions at the Best Sports Betting Sites Reviewed\", locate the first two words.": "Bookmaker sites",
    "Scroll to the section called \"Reload Bonuses\", locate the first two words.": "Once the",
    "Scroll to the section called \"Avoid Chasing Losses\", locate the first two words of the third sentence.": "if your",
    "Scroll to the section \"About SmartBettingGuide\", locate the words between \"find\" and \"betting\" in the last sentence.": "perfect sports",
    "Scroll to the section \"About SmartBettingGuide\", locate the fourth and fifth words of the third sentence.": "niche betting",
    "Scroll to the section called \"Betting Ratings\", locate the first 2 words.": "Crypto Betting",
    "Scroll to the section called \"Hours of Hands-on Testing\", locate the first 2 words.": "We spend",
    "Scroll to the section called \"Meet Our Expert Team\", locate the first 2 words.": "Zigmas Pekarskas",
    "Scroll to the section called \"Written Articles\", locate the last 2 words.": "and engaged",
    "Scroll to the section called \"About SmartBettingGuide\", locate the last 2 words.": "your needs",
    "Scroll to the section called \"Written Articles\", locate the sixth and seventh words of the description.": "diverse topics",
    "Scroll to the section called \"Useful Links\", locate the last 2 words.": "Complaints Policy",
    "Scroll to the section called \"Strategies & Bankroll Management When Betting with Crypto\", then to the sub-section \"Understand Volatility\", locate the sixth, seventh, eighth, and ninth words of the first sentence.": "move in price quickly",
    "Scroll to the section called \"Strategies & Bankroll Management When Betting with Crypto\", then to the sub-section \"Understand Volatility\", locate the last three words of the second sentence.": "one volatile coin",
    "Scroll to the section called \"Years of Research\", locate the last 2 words.": "and experience",
    "Scroll to the section called \"We Offer Knowledge & Education\", locate the second and third words of the second sentence.": "clear guides",
    "Scroll to the section called \"Our Mission\", locate the third and fourth words from the end of the second sentence.": "professional online"
}

# 3. WHEN BOT STARTS
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('Bot is online and ready with 128 triggers!')

# 4. WHEN SOMEONE SENDS A MESSAGE
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content.lower()
    
    for trigger, reply in AUTO_REPLIES.items():
        if trigger.lower() in msg:  # case-insensitive partial match
            await message.channel.send(reply)
            break 

# 5. RUN THE BOT - PASTE YOUR TOKEN HERE
client.run('MTUzOTMxNjA0MDcxNzMxMjE3NA.GX9cuk.r6Y-_a_iI0_EuJ6cRnGVU0RZgt8B__0MgJbTwM')