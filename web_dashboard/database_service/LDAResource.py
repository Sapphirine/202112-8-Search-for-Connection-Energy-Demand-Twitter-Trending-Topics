import os
import codecs


class LDAResource:
    def __init__(self):
        pass

    @classmethod
    def _run_lda(cls, start_date, end_date, areas):

        if type(areas) == list:
            formatted_area_list = [''.join(filter(str.isalpha, a.lower())) for a in areas]
            region_args = ','.join([a for a in formatted_area_list])     
        else:
            region_args = ''.join(x for x in areas.lower() if x.isalpha())
        
        tweets_dir = os.path.abspath('../tweets_data')

        command = f"""python main.py --start_date='{start_date}' --end_date='{end_date}' --region='{region_args}' --tweet_directory='{tweets_dir}'"""
        
        os.system(command)

        html_file = codecs.open("lda.html", 'r')
        
        return html_file.read()


    @classmethod
    def get_lda_result(cls, start_date, end_date, areas):
        
        store_dir = os.path.abspath('../web_dashboard')
        os.chdir(os.path.abspath('../lda'))

        html_text = LDAResource._run_lda(start_date, end_date, areas)

        os.chdir(store_dir)

        return(html_text)

