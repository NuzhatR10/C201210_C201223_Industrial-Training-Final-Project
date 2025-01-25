import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
# gro_api_key=os.getenv("GROQ_API_KEY")

def generate_summary(news_body):
    client = Groq()
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are expert in news summarization in bengali languages. Please summarize the following news article in top  3-5 bullet points in the bengali language that you get."
            },
            {
                "role": "user",
                "content": news_body
            }
        ],
        temperature=0,
        max_tokens=32768,
        top_p=1,
        stream=False,
        stop=None,
    )
    return chat_completion.choices[0].message.content




if __name__ == '__main__':
    data = generate_summary('''
            দ্বাদশ জাতীয় সংসদ নির্বাচনে নোয়াখালীর কোম্পানীগঞ্জে টাকা দিয়ে নারীদের লাইনে দাঁড় করিয়ে রাখা হয় বলে মন্তব্য করেছেন নোয়াখালীর কোম্পানীগঞ্জ উপজেলা আওয়ামী লীগের সভাপতি ও বসুরহাট পৌরসভার মেয়র আবদুল কাদের মির্জা। ভোটদান প্রক্রিয়ায় অনিয়মের কথা বলতে গিয়ে তিনি এ মন্তব্য করেন। তিনি বাংলাদেশ আওয়ামী লীগের সাধারণ সম্পাদক এবং সড়ক পরিবহন ও সেতুমন্ত্রী ওবায়দুল কাদেরের ছোট ভাই।

            গত ৭ জানুয়ারির দ্বাদশ জাতীয় সংসদ নির্বাচনে কোম্পানীগঞ্জ ও কবিরহাট উপজেলা নিয়ে গঠিত নোয়াখালী-৫ আসন থেকে টানা চতুর্থবারের মতো সংসদ সদস্য নির্বাচিত হয়েছেন ওবায়দুল কাদের। বিএনপি নির্বাচন না করলেও ওবায়দুল কাদেরের বিপক্ষে জাতীয় পার্টিসহ বিভিন্ন দলের চারজন প্রার্থী ছিলেন।

            আজ শুক্রবার বিকেলে বসুরহাট পৌরসভা মিলনায়তনে উপজেলা পরিষদের নবনির্বাচিত চেয়ারম্যান ও দুই ভাইস চেয়ারম্যানের সংবর্ধনা অনুষ্ঠানে প্রধান অতিথির বক্তৃতায় কাদের মির্জা ওই মন্তব্য করেন। কাদের মির্জার বক্তব্যটি দলের নেতা-কর্মীরা ফেসবুকে লাইভে প্রচার করেন।

            আবদুল কাদের মির্জা তাঁর বক্তৃতায় বলেন, ‘সদ্য সমাপ্ত উপজেলা পরিষদ নির্বাচনের চেয়েও বেশি অনিয়ম হয়েছে, ভোটের অনিয়ম না, আমাদের নেতা-কর্মীদের অনিয়ম হয়েছে গত পার্লামেন্ট নির্বাচনে। ১০-১৫ জন, ২০ জন নারী এনে ৫০০ টাকা ৫০০ টাকা করে দিয়ে দাঁড় করিয়ে রাখা হয়েছে। কোনো অফিসার কিংবা আমরা যখন যাই, সেখানে তখন তাঁদের দাঁড় করিয়ে দেওয়া হয়েছে। ভোট হয়েছে এই সিস্টেমে। মিথ্যা কথা বলেছি?...না। এবারের নির্বাচনে (উপজেলা পরিষদ) ওনারা (কাদের মির্জার প্রার্থীর প্রতিদ্বন্দ্বী প্রার্থী) অনিয়ম করেনি? চর কাঁকড়ার ৭ নম্বর ওয়ার্ডে এক ছেলে আমাদের সাথে থেকে ১০০ ভোট একসাথে মেরেছে দোয়াত-কলম প্রতীকে।’

            ওবায়দুল কাদেরের ছোট ভাই কাদের মির্জা বলেন, ‘আমাদের সমাজ থেকে একটা জিনিস আমরা দূর করতে পারিনি। সেটা হলো দুর্নীতি। দুর্নীতি আমাদের সমাজের রন্ধ্রে রন্ধ্রে ঢুকে গেছে। এই থেকে আমাদের সমাজকে রক্ষা করতে হবে, এর কোনো বিকল্প নেই। যে শিক্ষকদের সবচেয়ে বেশি সম্মান করত দেশের মানুষ, সেই শিক্ষাপ্রতিষ্ঠানগুলো আজকে সবচেয়ে বেশি দুর্নীতিতে ডুবে গেছে।’

            কাদের মির্জা বলেন, ‘থানায় গিয়ে কারও ইজ্জত-সম্মান থাকে না। টাকা দেবেন, আপনি ভদ্রলোক। টাকা দেবেন না আপনি বের হয়ে যান। একটা সালিসও তারা শেষ করতে পারে না। থানায় ঘুরতে ঘুরতে মানুষের স্যান্ডেলের তলা ক্ষয় হয়ে গেছে। বিচার নাই। মানুষ আজকে বিচার পায় না। ন্যায়বিচার প্রতিষ্ঠা করতে হবে, এটার বিকল্প নেই। ন্যায় কথা বলতে গিয়ে নিজের পরিবারের বিরুদ্ধে যদি যায়, সে কথা বলতে হবে নবনির্বাচিত তিন জনপ্রতিনিধিকে।’

            বসুরহাট পৌরসভার মেয়র আবদুল কাদের মির্জা নবনির্বাচিত চেয়ারম্যান ও ভাইস চেয়ারম্যানদের উদ্দেশ করে বলেন, ‘অন্যায়কারী আপনাদের ভাই হলেও তাকে কোনো দিন প্রশ্রয় দেবেন না। আমি আমার ভাইয়ের বিরুদ্ধে ইলেকশন করেছি, ওপরে আল্লাহ জানে। আমি করেছি মনেপ্রাণে। আমি করেছি ওবায়দুল কাদেরের সঙ্গে বেয়াদবির জন্য। আমার সাথে বেয়াদবির জন্য। আমরা যখন যার জন্য কাজ করি ইমানদারির সাথে করি।’

            সংবর্ধনা অনুষ্ঠানে আবদুল কাদের মির্জা ছাড়াও নবনির্বাচিত উপজেলা পরিষদের চেয়ারম্যান গোলাম শরীফ চৌধুরী, দুই ভাইস চেয়ারম্যান মুহাম্মদ জসিম উদ্দিন, পারভীন আক্তারসহ উপজেলা আওয়ামী লীগ নেতারা বক্তব্য দেন।
            ''')

    print(data)