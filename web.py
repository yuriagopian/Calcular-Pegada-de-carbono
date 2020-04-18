from flask import Flask, render_template, redirect, url_for, request

web = Flask(__name__)

@web.route("/")
def main():
    return render_template("index.html")
    
    
@web.route("/result", methods=['POST'])

def result():
    if request.method == 'POST':

        Variavel1 = request.form['Variavel1']
        if Variavel1 == '':
            Variavel1 = '0'

        Variavel2 = request.form['Variavel2']
        if Variavel2 == '':
            Variavel2 = '0'
            
        Variavel3 = request.form['Variavel3']
        if Variavel3 == '':
            Variavel3 = '0'
            
        Variavel4 = request.form['Variavel4']
        if Variavel4 == '':
            Variavel4 = '0'
            
        Variavel5 = request.form['Variavel5']
        if Variavel5 == '':
            Variavel5 = '0'
            
        Variavel6 = request.form['Variavel6']
        if Variavel6 == '':
            Variavel6 = '0'
            
        Variavel7 = request.form['Variavel7']
        if Variavel7 == '':
            Variavel7 = '0'
            
        Variavel8 = request.form['Variavel8']
        if Variavel8 == '':
            Variavel8 = '0'
            
        Variavel9 = request.form['Variavel9']
        if Variavel9 == '':
            Variavel9 = '0'
            
        Variavel10 = request.form['Variavel10']
        if Variavel10 == '':
            Variavel10 = '0'
            
        Variavel11 = request.form['Variavel11']
        if Variavel11 == '':
            Variavel11 = '0'
            
        Variavel12 = request.form['Variavel12']
        if Variavel12 == '':
            Variavel12 = '0'
            
        Variavel13 = request.form['Variavel13']
        if Variavel13 == '':
            Variavel13 = '0'
            
        Variavel14 = request.form['Variavel14']
        if Variavel14 == '':
            Variavel14 = '0'
            
        Variavel15 = request.form['Variavel15']
        if Variavel15 == '':
            Variavel15 = '0'
            
        Variavel16 = request.form['Variavel16']
        if Variavel16 == '':
            Variavel16 = '0'
            
        Variavel17 = request.form['Variavel17']
        if Variavel17 == '':
            Variavel17 = '0'
                        
        sum =  ((float(Variavel1) * 0.0003) + 
                (float(Variavel2) * 0.0359) + 
                (float(Variavel3) * 0.0227) +
                (float(Variavel4) * 0.0020) + 
                (float(Variavel5) * 0.0030) + 
                (float(Variavel6) * 0.0040) +
                (float(Variavel7) * 0.0010) +
                (float(Variavel8) * 0.0010) +
                (float(Variavel9) * 0.0010) +
                (float(Variavel10) * 0.0010) +
                (float(Variavel11) * 0.0030) +
                (float(Variavel12) * 0.0020) +
                (float(Variavel13) * 0.0010) +
                (float(Variavel14) * 0.0030) +
                (float(Variavel15) * 0.1603) +
                (float(Variavel16) * 2.25) +
                (float(Variavel17) * 0.9636))
                
    return render_template('index.html', 
                            sum=sum,)        
                      

web.run()
