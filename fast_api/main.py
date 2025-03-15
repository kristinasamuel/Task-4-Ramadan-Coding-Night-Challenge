#  fastapi is a modern, fast (high-performance), web framework for building APIs.
#  It is easy to use and requires less code to build APIs.

from fastapi import FastAPI
import random     # import random module to generate random side hustle ideas and money quotes

app =  FastAPI()

side_hustles = [

    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Shareyour knowledge and earn! ",
    "Print-end-Demand - Sell custom-designed products! ",
    "Blogging - Create content and earn through adds and sponsorships!",
    "Youtube Channel - Create content and earn through adds and sponsorships!",
    "Social Media Management - Manage account for  brands and influencers!",
    "Apps Development - Create mobile or web applications for businesses!",
]

money_quotes = [
       "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Opportunities don’t happen. You create them. – Chris Grosser",
    "Don’t stay in bed unless you can make money in bed. – George Burns",
    "Money often costs too much. – Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "It’s not about having lots of money. It’s about knowing how to manage it. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb",
]

# Implemented two new endpoints

# /side_hustlesfor random side hustle ideas
@app.get("/side_hustles")
def get_side_hustles(apikey:str):
    """Returns a random side hustle idea"""
    if apikey != "1234567890":
        return {"error": "Invalid api key"}
    return {"side_hustles": random.choice(side_hustles)}

#  /money_quotes for random money quotes
@app.get("/money_quotes")
def get_money_quotes(apikey:str):
    """return a random money quotes"""
    if apikey != "1234567890":
        return {"error": "Invalid api"}
    return {"money_quote": random.choice(money_quotes)} 
