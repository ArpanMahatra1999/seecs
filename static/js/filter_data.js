$(document).ready(function(){

    $("#dss").on('change', function(){
    var selectedDss = $(this).children("option:selected").val();
    filter_table(selectedDss)
    });

    $("#district").hide();
    $("#municipality").hide();

    function filter_table(value){

            $('table tbody tr').each(function(){

                var found='false';
                $(this).each(function(){

                    if($(this).text().toLowerCase().indexOf(value.toLowerCase()) >= 0){

                        found = 'true';
                    }
                });
                if(found == 'true'){
                    $(this).show();
                }
                else
                {
                    $(this).hide();
                }
            });
    }



    $("#province").on('change',function(){

        var selectedProvince = $(this).children("option:selected").val();
        filter_table(selectedProvince);
        getDistricts(selectedProvince)
        $("#district").on('change',function(){
                    var selectedDistrict = $(this).children("option:selected").val();

                    if(selectedDistrict===''){

                     filter_table(selectedProvince);
                        $("#municipality").hide();

                    }


                });
        });




    function getDistricts(selectedProvince){

        $("#province").on('change',function(){

            var selectedProvince = $(this).children("option:selected").val();

            if(selectedProvince===''){
                $("#district").hide();
                $("#municipality").hide();
            }

        });

        $("#district").show();
        $("#district").on('change',function(){
            var selectedDistrict = $(this).children("option:selected").val();
            filter_table(selectedDistrict);
            getMunicipality(selectedDistrict)

        });

         function removeOption(){

             $('#district option').each(function(){
                if(jQuery.inArray($(this).val(), districts)){
                 $('#district option').remove()
                }
             });
         }

        function appendOption(){
        $('#district').append(new Option("District","" ));
            for(var i=0; i<districts.length; i++){
                $('#district').append(new Option(districts[i].text,districts[i].value ));
            }

        }



        if(selectedProvince === "Province 1"){

            var districts = [

            {text:"Taplejung",value:"Taplejung"},
            {text:"Sankhuwasabha",value:"Sankhuwasabha"},
            {text:"Solukhumbu",value:"Solukhumbu"},
            {text:"Okhaldhunga",value:"Okhaldhunga"},
            {text:"Khotang",value:"Khotang"},
            {text:"Bhojpur",value:"Bhojpur"},
            {text:"Dhankuta",value:"Dhankuta"},
            {text:"Terhathum",value:"Terhathum"},
            {text:"Panchthar",value:"Panchthar"},
            {text:"Ilam",value:"Ilam"},
            {text:"Jhapa",value:"Jhapa"},
            {text:"Morang",value:"Morang"},
            {text:"Sunsari",value:"Jhapa"},
            ]

             removeOption()
             appendOption()



        }else if(selectedProvince === "Province 2"){


            var districts = [

             {text:"Saptari",value:"Saptari"},
             {text:"Siraha",value:"Siraha"},
             {text:"Dhunasa",value:"Dhunasa"},
             {text:"Mohattari",value:"Mohattari"},
             {text:"Sarlahi",value:"Sarlahi"},
             {text:"Rautahat",value:"Rautahat"},
             {text:"Bara",value:"Bara"},
             {text:"Parsa",value:"Parsa"},
            ]

          removeOption()

          appendOption()

        }

        else if(selectedProvince === "Bagmati Province"){

            var districts = [

             {text:"Dolakha",value:"Dolakha"},
             {text:"Sindhupalchok",value:"Sindhupalchok"},
             {text:"Rasuwa",value:"Rasuwa"},
             {text:"Dhading",value:"Dhading"},
             {text:"Nuwakot",value:"Nuwakot"},
             {text:"Kathmandu",value:"Kathmandu"},
             {text:"Bhaktapur",value:"Bhaktapur"},
             {text:"Lalitpur",value:"Lalitpur"},
             {text:"Kavrepalanchok",value:"Kavrepalanchok"},
             {text:"Ramechhap",value:"Ramechhap"},
             {text:"Sindhuli",value:"Sindhuli"},
             {text:"Makwanpur",value:"Makwanpur"},
             {text:"Chitwan",value:"Chitwan"},
            ]
          removeOption()
          appendOption()

        }
        else if(selectedProvince === "Gandaki Province"){
            var districts = [

             {text:"Gorkha",value:"Gorkha"},
             {text:"Manang",value:"Manang"},
             {text:"Mustang",value:"Mustang"},
             {text:"Myagdi",value:"Myagdi"},
             {text:"Kaski",value:"Kaski"},
             {text:"Lamjung",value:"Lamjung"},
             {text:"Tanahu",value:"Tanahu"},
             {text:"Nawalpur",value:"Nawalpur"},
             {text:"Syangja",value:"Syangja"},
             {text:"Parbat",value:"Parbat"},
             {text:"Baglung",value:"Baglung"},

            ]
          removeOption()
          appendOption()

        }

        else if(selectedProvince === "Lumbini Province"){
            var districts = [

             {text:"Rukum East",value:"Rukum East"},
             {text:"Rolpa",value:"Rolpa"},
             {text:"Pyuthan",value:"Pyuthan"},
             {text:"Gulmi",value:"Gulmi"},
             {text:"Arghakhanchi",value:"Arghakhanchi"},
             {text:"Palpa",value:"Palpa"},
             {text:"Parasi",value:"Parasi"},
             {text:"Rupandehi",value:"Rupandehi"},
             {text:"Kapilbastu",value:"Kapilbastu"},
             {text:"Dang",value:"Dang"},
             {text:"Banke",value:"Banke"},
             {text:"Bardiya",value:"Bardiya"},

            ]
          removeOption()
          appendOption()

        }

        else if(selectedProvince === "Karnali Province"){
            var districts = [

             {text:"Dolpa",value:"Dolpa"},
             {text:"Mugu",value:"Mugu"},
             {text:"Humla",value:"Humla"},
             {text:"Jumla",value:"Jumla"},
             {text:"Kalikot",value:"Kalikot"},
             {text:"Dailekh",value:"Dailekh"},
             {text:"Jajarkot",value:"Jajarkot"},
             {text:"Rukum West",value:"Rukum West"},
             {text:"Salyan",value:"Salyan"},
             {text:"Surkhet",value:"Surkhet"},
            ]
          removeOption()
          appendOption()

        }

        else if(selectedProvince === "Sudurpashchim Province"){
            var districts = [

             {text:"Bajura",value:"Bajura"},
             {text:"Bajhang",value:"Bajhang"},
             {text:"Darchula",value:"Darchula"},
             {text:"Baitadi",value:"Baitadi"},
             {text:"Dadeldhura",value:"Dadeldhura"},
             {text:"Doti",value:"Doti"},
             {text:"Achham",value:"Achham"},
             {text:"Kailali",value:"Kailali"},
             {text:"Kanchanpur",value:"Kanchanpur"},

            ]
          removeOption()
          appendOption()

        }
       }

        function getMunicipality(selectedProvince){
            $("#municipality").show();

             $("#district").on('change',function(){
                var selectedDistrict = $(this).children("option:selected").val();

                if(selectedDistrict===''){
                    $("#municipality").hide();
                }

                $("#municipality").on('change',function(){
                var selectedMunicipality = $(this).children("option:selected").val();
                if(selectedMunicipality===''){
                  filter_table(selectedDistrict);
                }

                });

             });

           function removeOption(){

             $('#municipality option').each(function(){
                if(jQuery.inArray($(this).val(), municipality)){
                 $('#municipality option').remove()
                }
             });
            }

            function appendOption(){
            $('#municipality').append(new Option("Municipality","" ));
                for(var i=0; i<municipality.length; i++){
                    $('#municipality').append(new Option(municipality[i].text,municipality[i].value ));
                }

            }

            $("#municipality").on('change',function(){
            var selectedMunicipality = $(this).children("option:selected").val();
                filter_table(selectedMunicipality);


            });
            if(selectedProvince==='Taplejung'){
               var municipality =  [

                 {text:"Phaktanlung ",value:"Phaktanlung "},
                 {text:"Mikwakhola ",value:"Mikwakhola" },
                 {text:"Meringden" ,value:"Meringden "},
                 {text:"Maiwakhola ",value:"Maiwakhola "},
                 {text:"Aatharai Tribeni" ,value:"Aatharai Tribeni "},
                 {text:"Phungling",value:"Phungling"},
                 {text:"Yangwarak" ,value:"Yangwarak "},
                 {text:"Sirijanga" ,value:"Sirijanga "},
                 {text:"Sidingba" ,value:"Sidingba" },

               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Sankhuwasabha'){
               var municipality =  [

                 {text:"Bhotkhola ",value:"Bhotkhola" },
                 {text:"Makalu ",value:"Makalu "},
                 {text:"Silichong" ,value:"Silichong" },
                 {text:"Chichila ",value:"Chichila "},
                 {text:"Sabhapokhari" ,value:"Sabhapokhari" },
                 {text:"Khandabari",value:"Khandabari"},
                 {text:"Panchakhapan",value:"Panchakhapan"},
                 {text:"Chainapur",value:"Chainapur"},
                {text:"Madi",value:"Madi"},
                {text:"Dharmadevi",value:"Dharmadevi"},

               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Solukhumbu'){
               var municipality =  [

                 {text:"Khumbu Pasanglhamu ",value:"Khumbu Pasanglhamu "},
                 {text:"Mahakulung" ,value:"Mahakulung" },
                 {text:"Sotang" ,value:"Sotang" },
                 {text:"Dhudhakoshi ",value:"Dhudhakoshi" },
                 {text:"Dhudha Koushika ",value:"Dhudha Koushika" },
                 {text:"Necha Salyan ",value:"Necha Salyan" },
                 {text:"Solu Dhudhakunda",value:"Solu Dhudhakunda"},
                 {text:"Likhu Pike ",value:"Likhu Pike"},

               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Okhaldhunga'){
               var municipality =  [

                 {text:"Chishankhu Gadhi" ,value:"Chishankhu Gadhi" },
                 {text:"Siddhicharan",value:"Siddhicharan"},
                 {text:"Molung ",value:"Molung" },
                 {text:"Khiji Demba ",value:"Khiji Demba" },
                 {text:"Likhu ",value:"Likhu" },
                 {text:"Champadevi ",value:"Champadevi "},
                 {text:"Sunkoshi" ,value:"Sunkoshi" },
                 {text:"Manebhanjyang" ,value:"Manebhanjyang" },

               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Khotang'){
               var municipality =  [

                 {text:"Kepilasgadhi" ,value:"Kepilasgadhi" },
                 {text:"Aiselukharka" ,value:"Aiselukharka" },
                 {text:"Lamidanda ",value:"Lamidanda" },
                 {text:"Halesi Tuwachung",value:"Halesi Tuwachung"},
                 {text:"Rupakot Majhuwagadhi",value:"Rupakot Majhuwagadhi"},
                 {text:"Sakela" ,value:"Sakela "},
                 {text:"Diprung" ,value:"Diprung "},
                 {text:"Khotehang ",value:"Khotehang" },
                {text:"Jante Dhunga ",value:"Jante Dhunga" },
                {text:"Baraha Pokhari" ,value:"Baraha Pokhari" },

               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Bhojpur'){
               var municipality =  [

                 {text:"Shadananda",value:"Shadananda"},
                 {text:"Salpa Silichho" ,value:"Salpa Silichho" },
                 {text:"Tyamke Maiyum ",value:"Tyamke Maiyum" },
                 {text:"Bhojpur",value:"Bhojpur"},
                 {text:"Arun ",value:"Arun" },
                 {text:"Pauwa Dunma ",value:"Pauwa Dunma" },
                 {text:"Ramprasad Rai" ,value:"Ramprasad Rai "},
                 {text:"Hatuwagadhi" ,value:"Hatuwagadhi "},
                {text:"Aamchowk ",value:"Aamchowk" },
               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Dhankuta'){
               var municipality =  [

                 {text:"Mahalaxmi",value:"Mahalaxmi"},
                 {text:"Pakhribas",value:"Pakhribas"},
                 {text:"Chhathar Jorpati ",value:"Chhathar Jorpati "},
                 {text:"Dhankuta",value:"Dhankuta"},
                 {text:"Khalsa Chhintang Sahidbhumi ",value:"Khalsa Chhintang Sahidbhumi" },
                 {text:"Sangurigadhi ",value:"Sangurigadhi "},
                 {text:"Chaubise" ,value:"Chaubise "},


               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Terhathum'){
               var municipality =  [

                 {text:"Aatharai ",value:"Aatharai" },
                 {text:"Phedap" ,value:"Phedap" },
                 {text:"Menchhayayem ",value:"Menchhayayem" },
                 {text:"Myanglung",value:"Myanglung"},
                 {text:"Laligurans",value:"Laligurans"},
                 {text:"Chhathar" ,value:"Chhathar" },

               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Panchthar'){
               var municipality =  [

                 {text:"Yangbarak ",value:"Yangbarak "},
                 {text:"Hilihan" ,value:"Hilihan "},
                 {text:"Falelung ",value:"Falelung" },
                 {text:"Phidim",value:"Phidim"},
                 {text:"Falgunanda ",value:"Falgunanda "},
                 {text:"Kummayak" ,value:"Kummayak" },
                 {text:"Tumbewa" ,value:"Tumbewa" },
                 {text:"Miklajung" ,value:"Miklajung"},
               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Ilam'){
               var municipality =  [

                 {text:"Mai Jogmai" ,value:"Mai Jogmai" },
                 {text:"Sandakpur ",value:"Sandakpur" },
                 {text:"Ilam",value:"Ilam"},
                 {text:"Deumai",value:"Deumai"},
                 {text:"Fakfokathum" ,value:"Fakfokathum" },
                 {text:"Mangsebung" ,value:"Mangsebung "},
                 {text:"Chulachuli ",value:"Chulachuli "},
                 {text:"Mai",value:"Mai"},
                {text:"Suryodaya",value:"Suryodaya"},
                {text:"Rong ",value:"Rong "},


               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Jhapa'){
               var municipality =  [

                 {text:"Mechinagar",value:"Mechinagar"},
                 {text:"Buddhashanti ",value:"Buddhashanti" },
                 {text:"Arjundhara",value:"Arjundhara"},
                 {text:"Kankai",value:"Kankai"},
                 {text:"Shivasatakshi",value:"Shivasatakshi"},
                 {text:"Kamal ",value:"Kamal "},
                 {text:"Damak",value:"Damak"},
                 {text:"Gauradaha",value:"Gauradaha"},
                {text:"Gauriganj ",value:"Gauriganj" },
                {text:"Jhapa" ,value:"Jhapa" },
                {text:"Barhadashi ", value:"Barhadashi" },
                {text:"Birtamod", value:"Birtamod"},
                {text:"Haldibari" , value:"Haldibari "},
                {text:"Bhadrapur", value:"Bhadrapur"},
                {text:"Kachanakawal ", value:"Kachanakawal "},




               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Morang'){
               var municipality =  [

                 {text:"Miklajung" , value:"Miklajung" },
                 {text:"Letang", value:"Letang"},
                 {text:"Kerabari" , value:"Kerabari "},
                 {text:"Sundarharaicha", value:"Sundarharaicha"},
                 {text:"Belbari", value:"Belbari"},
                 {text:"Kanepokhari ", value:"Kanepokhari "},
                 {text:"Pathari Shanishchare", value:"Pathari Shanishchare"},
                 {text:"Urlabari", value:"Urlabari"},
                 {text:"Ratuwamai", value:"Ratuwamai"},
                 {text:"Sunwarshi", value:"Sunwarshi"},
                 {text:"Rangeli", value:"Rangeli"},
                 {text:"Gramthan ", value:"Gramthan" },
                 {text:"Budhiganga ", value:"Budhiganga" },
                 {text:"Biratnagar ", value:"Biratnagar "},
                 {text:"Katahari ", value:"Katahari" },
                 {text:"Dhanapalthan ", value:"Dhanapalthan" },
                 {text:"Jahada ", value:"Jahada" }




               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Sunsari'){
               var municipality =  [

                 {text:"Dharan ", value:"Dharan "},
                 {text:"Baraha", value:"Baraha"},
                 {text:"Koshi" , value:"Koshi "},
                 {text:"Bhokraha" , value:"Bhokraha" },
                 {text:"Ramdhuni", value:"Ramdhuni"},
                 {text:"Itahari ", value:"Itahari "},
                 {text:"Duhabi", value:"Duhabi"},
                 {text:"Gadhi ", value:"Gadhi" },
                 {text:"Inaruwa", value:"Inaruwa"},
                 {text:"Harinagara" , value:"Harinagara "},
                 {text:"Dewangunj" , value:"Dewangunj" },
                 {text:"Barju ", value:"Barju" },


               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Udayapur'){
               var municipality =  [

                 {text:"Chaudandigadhi", value:"Chaudandigadhi"},
                 {text:"Triyuga", value:"Triyuga"},
                 {text:"Rautamai" , value:"Rautamai" },
                 {text:"Sunkoshi ", value:"Sunkoshi" },
                 {text:"Tapli" , value:"Tapli" },
                 {text:"Katari", value:"Katari"},
                 {text:"Udayapurgadhi ", value:"Udayapurgadhi" },


               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Saptari'){
               var municipality =  [

                 {text:"Saptakoshi", value:"Saptakoshi"},
                 {text:"Kanchanrup", value:"Kanchanrup"},
                 {text:"Agnisair Krishna Sabaran" , value:"Agnisair Krishna Sabaran "},
                 {text:"Rupani ", value:"Rupani" },
                 {text:"Shambhunath", value:"Shambhunath"},
                 {text:"Khadak", value:"Khadak"},
                 {text:"Surunga", value:"Surunga"},
                 {text:"Balan-Bihul ", value:"Balan-Bihul" },
                 {text:"BodeBarsain", value:"BodeBarsain"},
                 {text:"Dakneshwori", value:"Dakneshwori"},
                 {text:"Belhi Chapena ", value:"Belhi Chapena" },
                 {text:"Bishnupur" , value:"Bishnupur" },
                 {text:"Rajbiraj", value:"Rajbiraj"},
                 {text:"Mahadewa ", value:"Mahadewa" },
                 {text:"Tirahut ", value:"Tirahut "},
                 {text:"Hanumannagar Kankalini", value:"Hanumannagar Kankalini"},
                 {text:"Tilathi Koiladi ", value:"Tilathi Koiladi "},
                 {text:"Chhinnamasta ", value:"Chhinnamasta "},

               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Siraha'){
               var municipality =  [

                 {text:"Lahan", value:"Lahan"},
                 {text:"Dhangadhimai", value:"Dhangadhimai"},
                 {text:"Golbazar", value:"Golbazar"},
                 {text:"Mirchaiya", value:"Mirchaiya"},
                 {text:"Karjanha", value:"Karjanha"},
                 {text:"Kalyanpur", value:"Kalyanpur"},
                 {text:"Naraha" , value:"Naraha "},
                 {text:"Bishnupur ", value:"Bishnupur" },
                 {text:"Arnama ", value:"Arnama" },
                 {text:"Sukhipur", value:"Sukhipur"},
                 {text:"Laxmipur Patari" , value:"Laxmipur Patari" },
                 {text:"Sakhuwa Nankarkatti" , value:"Sakhuwa Nankarkatti" },
                 {text:"Bhagawanpur" , value:"Bhagawanpur" },
                 {text:"Nawarajpur ", value:"Nawarajpur "},
                 {text:"Bariyarpatti ", value:"Bariyarpatti "},
                 {text:"Aurahi ", value:"Aurahi" },
                 {text:"Siraha", value:"Siraha"},

               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Dhunasa'){
               var municipality =  [

                  {text:"Ganeshman Charnath", value:"Ganeshman Charnath"},
                 {text:"Dhanushadham", value:"Dhanushadham"},
                  {text:"Mithila", value:"Mithila"},
                 {text:"Bateshwor ", value:"Bateshwor" },
                 {text:"Chhireshwornath", value:"Chhireshwornath"},
                 {text:"Laxminiya ", value:"Laxminiya" },
                  {text:"Mithila Bihari", value:"Mithila Bihari"},
                 {text:"Hansapur", value:"Hansapur"},
                  {text:"Sabaila", value:"Sabaila"},
                 {text:"Shahidnagar", value:"Shahidnagar"},
                  {text:"Kamala", value:"Kamala"},
                 {text:"Janak Nandini ", value:"Janak Nandini "},
                  {text:"Bideha", value:"Bideha"},
                 {text:"Aurahi ", value:"Aurahi" },
                  {text:"Janakpur ", value:"Janakpur "},
                 {text:"Dhanauji" , value:"Dhanauji" },
                  {text:"Nagarain", value:"Nagarain"},
                 {text:"Mukhiyapatti Musaharmiya" , value:"Mukhiyapatti Musaharmiya" },

               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Mohattari'){
               var municipality =  [

                 {text:"Bardibas", value:"Bardibas"},
                 {text:"Gaushala", value:"Gaushala"},
                  {text:"Sonama" , value:"Sonama" },
                 {text:"Aurahi", value:"Aurahi"},
                {text:"Bhangaha", value:"Bhangaha"},
                 {text:"Loharpatti", value:"Loharpatti"},
                  {text:"Balawa", value:"Balawa"},
                 {text:"Ram Gopalpur", value:"Ram Gopalpur"},
                {text:"Samsi" , value:"Samsi" },
                 {text:"Manara Shisawa", value:"Manara Shisawa"},
                  {text:"Ekadara" , value:"Ekadara" },
                 {text:"Mahottari" , value:"Mahottari "},
                {text:"Pipara" , value:"Pipara" },
                 {text:"Matihani", value:"Matihani"},
                  {text:"Jaleshwor", value:"Jaleshwor"},


               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Sarlahi'){
               var municipality =  [

                 {text:"Lalbandi", value:"Lalbandi"},
                {text:"Hariwan", value:"Hariwan"},
                 {text:"Bagmati", value:"Bagmati"},
                  {text:"Barahathawa", value:"Barahathawa"},
                 {text:"Haripur", value:"Haripur"},
                {text:"Ishworpur", value:"Ishworpur"},
                 {text:"Haripurwa", value:"Haripurwa"},
                  {text:"Parsa ", value:"Parsa" },
                 {text:"Brahmapuri ", value:"Brahmapuri "},
                {text:"Chandranagar ", value:"Chandranagar" },
                {text:"Kabilashi", value:"Kabilashi"},
                 {text:"Chakraghatta ", value:"Chakraghatta" },
                  {text:"Basbariya ", value:"Basbariya" },
                 {text:"Dhanakaul" , value:"Dhanakaul" },
                {text:"Ramnagar ", value:"Ramnagar "},
                 {text:"Balara", value:"Balara"},
                  {text:"Godaita", value:"Godaita"},
                 {text:"Bishnu ", value:"Bishnu" },
                {text:"Kaudena ", value:"Kaudena" },
                {text:"Malangawa", value:"Malangawa"},

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Rautahat'){
               var municipality =  [

                 {text:"Chandrapur", value:"Chandrapur"},
                  {text:"Gujara", value:"Gujara"},
                 {text:"Phatuwa Bijayapur", value:"Phatuwa Bijayapur"},
                {text:"Katahariya", value:"Katahariya"},
                 {text:"Brindaban", value:"Brindaban"},
                  {text:"Gadhimai", value:"Gadhimai"},
                 {text:"Madhav Narayan", value:"Madhav Narayan"},
                {text:"Garuda", value:"Garuda"},
                {text:"Dewahi Gonahi", value:"Dewahi Gonahi"},
                 {text:"Maulapur", value:"Maulapur"},
                  {text:"Boudhimai", value:"Boudhimai"},
                 {text:"Paroha", value:"Paroha"},
                {text:"Rajpur", value:"Rajpur"},
                 {text:"Yamunamai" , value:"Yamunamai "},
                  {text:"Durga Bhagawati ", value:"Durga Bhagawati" },
                 {text:"Rajdevi", value:"Rajdevi"},
                  {text:"Gaur", value:"Gaur"},
                  {text:"Ishanath", value:"Ishanath"}
               ]

                removeOption()

              appendOption()

            }
            else if(selectedProvince==='Bara'){
               var municipality =  [


                 {text:"Nijagadh", value:"Nijagadh"},
                  {text:"Kolhabi", value:"Kolhabi"},
                 {text:"Jitpur Simara ", value:"Jitpur Simara "},
                {text:"Parawanipur ", value:"Parawanipur" },
                 {text:"Prasauni", value:"Prasauni "},
                  {text:"Bishrampur ", value:"Bishrampur "},
                 {text:"Pheta" , value:"Pheta "},
                {text:"Kalaiya ", value:"Kalaiya "},
                {text:"Karaiyamai ", value:"Karaiyamai "},
                 {text:"Baragadhi ", value:"Baragadhi "},
                  {text:"Aadarsha Kotwal" , value:"Aadarsha Kotwal" },
                 {text:"Simroungadh", value:"Simroungadh"},
                {text:"Pacharauta", value:"Pacharauta"},
                 {text:"Mahagadhimai", value:"Mahagadhimai"},
                  {text:"Devtal ", value:"Devtal" },
                 {text:"Subarna ", value:"Subarna" },


               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Parsa'){
               var municipality =  [


                 {text:"Thori" , value:"Thori" },
                  {text:"Jirabhawani ", value:"Jirabhawani "},
                 {text:"Jagarnathpur ", value:"Jagarnathpur" },
                {text:"Paterwa Sugauli ", value:"Paterwa Sugauli" },
                 {text:"Sakhuwa Prasauni ", value:"Sakhuwa Prasauni" },
                  {text:"Parsagadhi", value:"Parsagadhi"},
                 {text:"Birgunj ", value:"Birgunj"},
                {text:"Bahudarmai", value:"Bahudarmai"},
                {text:"Pokhariya", value:"Pokhariya"},
                 {text:"Kalikamai ", value:"Kalikamai "},
                  {text:"Dhobini" , value:"Dhobini "},
                 {text:"Chhipaharmai ", value:"Chhipaharmai "},
                {text:"Pakaha Mainpur ", value:"Pakaha Mainpur "},
                 {text:"Bindabasini ", value:"Bindabasini "},
                  {text:"", value:""},
                 {text:"", value:""},


               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Dolakha'){
               var municipality =  [


                 {text:"Gaurishankar" , value:"Gaurishankar" },
                  {text:"Bigu ", value:"Bigu" },
                 {text:"Kalinchowk ", value:"Kalinchowk "},
                {text:"Baitedhar ", value:"Baitedhar" },
                 {text:"Jiri", value:"Jiri"},
                  {text:"Tamakoshi ", value:"Tamakoshi "},
                 {text:"Melung ", value:"Melung "},
                {text:"Shailung" , value:"Shailung" },
                {text:"Bhimeshwor", value:"Bhimeshwor"},


               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Sindhupalchok'){
               var municipality =  [


                 {text:"Bhotekoshi ", value:"Bhotekoshi" },
                  {text:"Jugal" , value:"Jugal" },
                 {text:"Panchpokhari Thangpal" , value:"Panchpokhari Thangpal" },
                {text:"Helambu ", value:"Helambu" },
                 {text:"Melanchi", value:"Melanchi"},
                  {text:"Indrawoti" , value:"Indrawoti" },
                 {text:"Choutara Sangachowkgadhi", value:"Choutara Sangachowkgadhi"},
                {text:"Balephi ", value:"Balephi "},
                {text:"Bahrabise", value:"Bahrabise"},
                 {text:"Tripurasundari ", value:"Tripurasundari "},
                  {text:"Lisankhu Pakhar" , value:"Lisankhu Pakhar" },
                 {text:"Sunkoshi" , value:"Sunkoshi" },

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Rasuwa'){
               var municipality =  [


                 {text:"Gosaikunda" , value:"Gosaikunda" },
                  {text:"Parbatikunda ", value:"Parbatikunda" },
                 {text:"Uttargaya" , value:"Uttargaya" },
                {text:"Kalika ", value:"Kalika "},
                 {text:"Naukunda ", value:"Naukunda" },

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Dhading'){
               var municipality =  [


                 {text:"Rubi Valley ", value:"Rubi Valley "},
                  {text:"Khaniyabas ", value:"Khaniyabas" },
                 {text:"Ganga Jamuna ", value:"Ganga Jamuna "},
                {text:"Tripurasundari ", value:"Tripurasundari" },
                 {text:"Netrawati" , value:"Netrawati "},
                  {text:"Nilkhantha", value:"Nilkhantha"},
                 {text:"Jwalamukhi ", value:"Jwalamukhi" },
                {text:"Siddhalek ", value:"Siddhalek" },
                {text:"Benighat Rorang ", value:"Benighat Rorang" },
                 {text:"Gajuri ", value:"Gajuri" },
                  {text:"Galchhi ", value:"Galchhi" },
                 {text:"Thakre" , value:"Thakre" },
                {text:"Dhunibenshi", value:"Dhunibenshi"},



               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Nuwakot'){
               var municipality =  [


                 {text:"Dupcheshwor" , value:"Dupcheshwor" },
                  {text:"Tadi ", value:"Tadi" },
                 {text:"Suryagadhi ", value:"Suryagadhi "},
                {text:"Bidur", value:"Bidur"},
                 {text:"Kispang" , value:"Kispang" },
                  {text:"Meghang ", value:"Meghang" },
                 {text:"Tarakeshwor ", value:"Tarakeshwor" },
                {text:"Belkotgadhi", value:"Belkotgadhi"},
                {text:"Likhu ", value:"Likhu" },
                 {text:"Panchakanya ", value:"Panchakanya" },
                  {text:"Shivapuri ", value:"Shivapuri "},
                 {text:"Kakani" , value:"Kakani" },

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Kathmandu'){
               var municipality =  [


                 {text:"Shankharapur", value:"Shankharapur"},
                  {text:"Kageshwori Manahara", value:"Kageshwori Manahara"},
                 {text:"Gokarneshwor", value:"Gokarneshwor"},
                {text:"Budhanilkhantha", value:"Budhanilkhantha"},
                 {text:"Tokha", value:"Tokha"},
                  {text:"Tarakeshwor", value:"Tarakeshwor"},
                 {text:"Nagarjun", value:"Nagarjun"},
                {text:"Kathmandu ", value:"Kathmandu "},
                {text:"Kirtipur", value:"Kirtipur"},
                 {text:"Chandragiri", value:"Chandragiri"},
                  {text:"Dakshinkali", value:"Dakshinkali"},

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Bhaktapur'){
               var municipality =  [


                 {text:"Changunarayan", value:"Changunarayan"},
                  {text:"Bhaktapur", value:"Bhaktapur"},
                 {text:"Madhyapur Thimi", value:"Madhyapur Thimi"},
                {text:"Suryabinayak", value:"Suryabinayak"},



               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Lalitpur'){
               var municipality =  [


                 {text:"Mahalaxmi", value:"Mahalaxmi"},
                  {text:"Lalitpur ", value:"Lalitpur "},
                 {text:"Godawari", value:"Godawari"},
                {text:"Konjyosom ", value:"Konjyosom "},
                 {text:"Mahankal ", value:"Mahankal" },
                  {text:"Bagmati ", value:"Bagmati" },

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Kavrepalanchok'){
               var municipality =  [


                 {text:"Chauri Deurali" , value:"Chauri Deurali "},
                  {text:"Bhumlu" , value:"Bhumlu" },
                 {text:"Mandan Deupur", value:"Mandan Deupur"},
                {text:"Banepa", value:"Banepa"},
                 {text:"Dhulikhel", value:"Dhulikhel"},
                  {text:"Panchkhal", value:"Panchkhal"},
                 {text:"Temal ", value:"Temal" },
                {text:"Namobuddha", value:"Namobuddha"},
                {text:"Panauti", value:"Panauti"},
                 {text:"Bethanchowk" , value:"Bethanchowk "},
                  {text:"Roshi ", value:"Roshi "},
                 {text:"Mahabharat ", value:"Mahabharat "},
                {text:"Khanikhola ", value:"Khanikhola" },


               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Ramechhap'){
               var municipality =  [


                 {text:"Umakunda" , value:"Umakunda" },
                  {text:"Gokulganga ", value:"Gokulganga" },
                 {text:"Likhu" , value:"Likhu "},
                {text:"Ramechhap", value:"Ramechhap"},
                 {text:"Manthali", value:"Manthali"},
                  {text:"Khandadevi ", value:"Khandadevi" },
                 {text:"Doramba" , value:"Doramba "},
                {text:"Sunapati" , value:"Sunapati" },

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Sindhuli'){
               var municipality =  [


                 {text:"Dudhouli", value:"Dudhouli"},
                  {text:"Phikkal ", value:"Phikkal" },
                 {text:"Tinpatan" , value:"Tinpatan" },
                {text:"Golanjor ", value:"Golanjor "},
                 {text:"Kamalamai", value:"Kamalamai"},
                  {text:"Sunkoshi ", value:"Sunkoshi" },
                 {text:"Ghyanglekha ", value:"Ghyanglekha" },
                {text:"Marin ", value:"Marin "},
                {text:"Hariharpurgaghi ", value:"Hariharpurgaghi" },

                {text:"", value:""},
                 {text:"", value:""},
                  {text:"", value:""},
                 {text:"", value:""},


               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Makwanpur'){
               var municipality =  [

                    {text:"Indrasarowar" , value:"Indrasarowar" },
                  {text:"Thaha", value:"Thaha"},
                 {text:"Kailash ", value:"Kailash" },
                 {text:"Raksirang" , value:"Raksirang "},
                  {text:"Manahari" , value:"Manahari" },
                 {text:"Hetauda ", value:"Hetauda "},
                {text:"Bhimphedi" , value:"Bhimphedi "},
                 {text:"Makawanpurgadhi ", value:"Makawanpurgadhi "},
                  {text:"Bakaiya ", value:"Bakaiya "},
                 {text:"Bagmati" , value:"Bagmati" },

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Chitwan'){
               var municipality =  [


                 {text:"Rapti", value:"Rapti"},
                  {text:"Kalika", value:"Kalika"},
                 {text:"Ichchha Kamana" , value:"Ichchha Kamana "},
                {text:"Bharatpur ", value:"Bharatpur "},
                 {text:"Ratnanagar", value:"Ratnanagar"},
                  {text:"Khairahani", value:"Khairahani"},
                 {text:"Madi", value:"Madi"},

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Gorkha'){
               var municipality =  [


                 {text:"Chumanubri ", value:"Chumanubri" },
                  {text:"Ajirkot", value:"Ajirkot" },
                 {text:"Sulikot" , value:"Sulikot" },
                {text:"Dharche" , value:"Dharche" },
                 {text:"Aarughat" , value:"Aarughat" },
                  {text:"Bhimsen" , value:"Bhimsen "},
                 {text:"Siranchowk ", value:"Siranchowk" },
                {text:"Palungtar", value:"Palungtar"},
                {text:"Gorkha", value:"Gorkha"},
                 {text:"Shahid Lakhan ", value:"Shahid Lakhan" },
                  {text:"Gandaki" , value:"Gandaki" },

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Manang'){
               var municipality =  [


                 {text:"Naraphu ", value:"Naraphu" },
                  {text:"Neshang ", value:"Neshang "},
                 {text:"Chame" , value:"Chame "},
                {text:"Nashong ", value:"Nashong" },


               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Mustang'){
               var municipality =  [


                {text:"Dalome ", value:"Dalome" },
                  {text:"Gharpajhong ", value:"Gharpajhong" },
                 {text:"Bahragaun Muktikshetra ", value:"Bahragaun Muktikshetra" },
                 {text:"Lomanthang ", value:"Lomanthang "},
                  {text:"Thasang" , value:"Thasang" },

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Myagdi'){
               var municipality =  [


                 {text:"Annapurna ", value:"Annapurna" },
                 {text:"Raghuganga" , value:"Raghuganga "},
                 {text:"Dhawalagiri ", value:"Dhawalagiri "},
                 {text:"Malika ", value:"Malika" },
                 {text:"Mangala ", value:"Mangala" },
                 {text:"Beni", value:"Beni"},

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Kaski'){
               var municipality =  [


                 {text:"Madi ", value:"Madi" },
                  {text:"Machhapuchchhre ", value:"Machhapuchchhre" },
                 {text:"Annapurna ", value:"Annapurna" },
                {text:"Pokhara Lekhnath ", value:"Pokhara Lekhnath "},
                 {text:"Rupa ", value:"Rupa" },


               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Lamjung'){
               var municipality =  [


                 {text:"Dordi ", value:"Dordi "},
                  {text:"Marshyangdi ", value:"Marshyangdi "},
                 {text:"Kwhola Sothar ", value:"Kwhola Sothar" },
                {text:"Madhya Nepal", value:"Madhya Nepal"},
                 {text:"Bensi Shahar", value:"Bensi Shahar"},
                  {text:"Sundarbazar", value:"Sundarbazar"},
                 {text:"Rainas", value:"Rainas"},
                {text:"Dudhapokhari" , value:"Dudhapokhari" },

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Tanahu'){
               var municipality =  [


                 {text:"Bhanu", value:"Bhanu"},
                  {text:"Byas", value:"Byas"},
                 {text:"Myagde ", value:"Myagde" },
                {text:"Shuklagandaki", value:"Shuklagandaki"},
                 {text:"Bhimad", value:"Bhimad"},
                  {text:"Ghiring ", value:"Ghiring" },
                 {text:"Rhishing ", value:"Rhishing" },
                {text:"Devghat ", value:"Devghat" },
                {text:"Bandipur ", value:"Bandipur" },
                 {text:"Aanbu Khaireni ", value:"Aanbu Khaireni" },



               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Nawalpur'){
               var municipality =  [


                 {text:"Gaidakot", value:"Gaidakot"},
                  {text:"Bulingtar ", value:"Bulingtar "},
                 {text:"Bungdikali ", value:"Bungdikali "},
                {text:"Hupsekot ", value:"Hupsekot "},
                 {text:"Devchuli", value:"Devchuli"},
                  {text:"Kawasoti", value:"Kawasoti"},
                 {text:"Madhya Bindu", value:"Madhya Bindu"},
                {text:"Binayi Tribeni ", value:"Binayi Tribeni "},

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Syangja'){
               var municipality =  [


                 {text:"Putalibazar", value:"Putalibazar"},
                  {text:"Phedikhola ", value:"Phedikhola" },
                 {text:"Aandhikhola ", value:"Aandhikhola" },
                {text:"Arjun Choupari ", value:"Arjun Choupari" },
                 {text:"Bhirkot Municipaity", value:"Bhirkot Municipaity"},
                  {text:"Biruwa ", value:"Biruwa" },
                 {text:"Harinas ", value:"Harinas "},
                {text:"Chapakot", value:"Chapakot"},
                {text:"Walling", value:"Walling"},
                 {text:"Galyang", value:"Galyang"},
                  {text:"Kaligandaki ", value:"Kaligandaki" },

               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Parbat'){
               var municipality =  [


                 {text:"Modi ", value:"Modi" },
                  {text:"Jaljala ", value:"Jaljala" },
                 {text:"Kushma", value:"Kushma"},
                {text:"Phalebas", value:"Phalebas"},
                 {text:"Mahashila ", value:"Mahashila "},
                  {text:"Bihadi ", value:"Bihadi" },
                 {text:"Paiyu ", value:"Paiyu" },


               ]

                removeOption()

                appendOption()
            }

            else if(selectedProvince==='Baglung'){
               var municipality =  [


                 {text:"Baglung", value:"Baglung"},
                  {text:"Kathekhola" , value:"Kathekhola" },
                 {text:"Tarakhola ", value:"Tarakhola" },
                {text:"Tamankhola" , value:"Tamankhola "},
                 {text:"Dhorpatan", value:"Dhorpatan"},
                  {text:"Nisikhola ", value:"Nisikhola" },
                 {text:"Badigad" , value:"Badigad" },
                {text:"Galkot", value:"Galkot"},
                {text:"Bareng ", value:"Bareng" },
                 {text:"Jaimuni", value:"Jaimuni"},

               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Rukum East'){
               var municipality =  [


                 {text:"Putha Uttanganga ", value:"Putha Uttanganga "},
                 {text:"Sisne" , value:"Sisne" },
                 {text:"Bhoome ", value:"Bhoome" },

               ]

                removeOption()

                appendOption()
            }
             else if(selectedProvince==='Rolpa'){
               var municipality =  [



                 {text:"Sunchhahari ", value:"Sunchhahari "},
                 {text:"Thawang" , value:"Thawang" },
                 {text:"Paribartan ", value:"Paribartan" },
                  {text:"Gangadev ", value:"Gangadev "},
                 {text:"Madi" , value:"Madi" },
                 {text:"Tribeni ", value:"Tribeni" },
                 {text:"Rolpa", value:"Rolpa"},
                 {text:"Runtigadhi" , value:"Runtigadhi "},
                 {text:"Sunil Smriti ", value:"Sunil Smriti" },
                 {text:"Lungri ", value:"Lungri" },


               ]

                removeOption()

                appendOption()
            }
            else if(selectedProvince==='Pyuthan'){
               var municipality =  [



                 {text:"Gaumukhi ", value:"Gaumukhi" },
                 {text:"Naubahini ", value:"Naubahini "},
                 {text:"Jhimaruk ", value:"Jhimaruk" },
                  {text:"Pyuthan", value:"Pyuthan"},
                 {text:"Sworgadwari", value:"Sworgadwari"},
                 {text:"Mandavi" , value:"Mandavi" },
                 {text:"Mallarani ", value:"Mallarani "},
                 {text:"Aairawati ", value:"Aairawati" },
                 {text:"Sarumarani ", value:"Sarumarani" },


               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Gulmi'){
               var municipality =  [



                 {text:"Kali Gandaki ", value:"Kali Gandaki" },
                 {text:"Satyawoti ", value:"Satyawoti "},
                 {text:"Chandrakot ", value:"Chandrakot" },
                  {text:"Musikot", value:"Musikot"},
                 {text:"Isma ", value:"Isma" },
                 {text:"Malika" , value:"Malika "},
                 {text:"Madane" , value:"Madane" },
                 {text:"Dhurkot" , value:"Dhurkot" },
                 {text:"Resunga", value:"Resunga"},
                 {text:"Gulmi Durbar ", value:"Gulmi Durbar "},
                 {text:"Chhatrakot", value:"Chhatrakot" },
                 {text:"Ruru ", value:"Ruru "},

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Arghakhanchi'){
               var municipality =  [



                 {text:"Chhatradev ", value:"Chhatradev "},
                 {text:"Malarani" , value:"Malarani" },
                 {text:"Bhumikasthan", value:"Bhumikasthan"},
                  {text:"Sandhikharka", value:"Sandhikharka"},
                 {text:"Panini ", value:"Panini "},
                 {text:"Shitaganga", value:"Shitaganga"},

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Palpa'){
               var municipality =  [



                 {text:"Rampur", value:"Rampur"},
                 {text:"Purbakhola" , value:"Purbakhola "},
                 {text:"Rambha" , value:"Rambha" },
                  {text:"Baganaskali ", value:"Baganaskali" },
                 {text:"Tansen", value:"Tansen"},
                 {text:"Ribdikot ", value:"Ribdikot" },
                 {text:"Rainadevi Chhahara ", value:"Rainadevi Chhahara" },
                 {text:"Tinau ", value:"Tinau" },
                 {text:"Mathagadhi" , value:"Mathagadhi" },
                 {text:"Nisdi ", value:"Nisdi" },



               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Parasi'){
               var municipality =  [



                 {text:"Bardaghat", value:"Bardaghat"},
                 {text:"Sunawal", value:"Sunawal"},
                 {text:"Ramgram", value:"Ramgram"},
                  {text:"Palhinandan ", value:"Palhinandan" },
                 {text:"Sarawal ", value:"Sarawal" },
                 {text:"Pratapapur ", value:"Pratapapur" },
                 {text:"Susta ", value:"Susta" },




               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Rupandehi'){
               var municipality =  [



                 {text:"Devdaha", value:"Devdaha"},
                 {text:"Butwal ", value:"Butwal "},
                 {text:"Sainamaina", value:"Sainamaina"},
                  {text:"Kanchan ", value:"Kanchan" },
                 {text:"Gaidahawa ", value:"Gaidahawa" },
                 {text:"Suddhodhan ", value:"Suddhodhan" },
                 {text:"Siyari ", value:"Siyari" },
                 {text:"Tilottama", value:"Tilottama"},
                 {text:"Om Satiya ", value:"Om Satiya" },
                 {text:"Rohini ", value:"Rohini" },
                 {text:"Siddharthanagar", value:"Siddharthanagar"},
                 {text:"Mayadevi ", value:"Mayadevi" },
                 {text:"Lumbini Sanskritik", value:"Lumbini Sanskritik"},
                 {text:"Kotahimai ", value:"Kotahimai" },
                 {text:"Sammarimai ", value:"Sammarimai "},
                 {text:"Marchawari ", value:"Marchawari "},

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Kapilbastu'){
               var municipality =  [



                 {text:"Banganga", value:"Banganga"},
                 {text:"Buddhabhumi", value:"Buddhabhumi"},
                 {text:"Shivaraj", value:"Shivaraj"},
                  {text:"Bijayanagar ", value:"Bijayanagar" },
                 {text:"Krishnanagar", value:"Krishnanagar"},
                 {text:"Maharajganj", value:"Maharajganj"},
                 {text:"Kapilbastu", value:"Kapilbastu"},
                 {text:"Yasodhara ", value:"Yasodhara "},
                 {text:"Mayadevi ", value:"Mayadevi" },
                 {text:"Shuddhodhan ", value:"Shuddhodhan" },

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Dang'){
               var municipality =  [



                 {text:"Bangalachuli ", value:"Bangalachuli" },
                 {text:"Ghorahi ", value:"Ghorahi "},
                 {text:"Tulsipur ", value:"Tulsipur "},
                  {text:"Shantinagar" , value:"Shantinagar" },
                 {text:"Babai ", value:"Babai "},
                 {text:"Dangisharan ", value:"Dangisharan" },
                 {text:"Lamahi", value:"Lamahi"},
                 {text:"Rapti" , value:"Rapti" },
                 {text:"Gadhawa" , value:"Gadhawa" },
                 {text:"Rajpur ", value:"Rajpur "},

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Banke'){
               var municipality =  [



                 {text:"Rapti Sonari ", value:"Rapti Sonari" },
                 {text:"Kohalpur", value:"Kohalpur"},
                 {text:"Baijanath ", value:"Baijanath" },
                  {text:"Khajura ", value:"Khajura" },
                 {text:"Janaki ", value:"Janaki" },
                 {text:"Nepalganj ", value:"Nepalganj "},
                 {text:"Duduwa ", value:"Duduwa" },
                 {text:"Narainapur ", value:"Narainapur" },


               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Bardiya'){
               var municipality =  [


                {text:"Bansgadhi", value:"Bansgadhi"},
                 {text:"Barbardiya", value:"Barbardiya"},
                 {text:"Thakurbaba", value:"Thakurbaba"},
                 {text:"Geruwa ", value:"Geruwa "},
                 {text:"Gulariya", value:"Gulariya"},
                 {text:"Badhaiyatal ", value:"Badhaiyatal" },

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Dolpa'){
               var municipality =  [



                 {text:"Dolpo Buddha ", value:"Dolpo Buddha" },
                 {text:"Shey Phoksundo ", value:"Shey Phoksundo "},
                 {text:"Jagadulla ", value:"Jagadulla "},
                  {text:"Mudkechula ", value:"Mudkechula "},
                 {text:"Tripurasundari", value:"Tripurasundari"},
                 {text:"Thulibheri", value:"Thulibheri"},
                 {text:"Kaike" , value:"Kaike" },
                 {text:"Chharka Tangsong ", value:"Chharka Tangsong "},


               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Mugu'){
               var municipality =  [



                 {text:"Mugumkarmarog ", value:"Mugumkarmarog" },
                 {text:"Chhayanath Rara", value:"Chhayanath Rara"},
                 {text:"Soru ", value:"Soru "},
                  {text:"Khatyad ", value:"Khatyad "},


               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Humla'){
               var municipality =  [


                 {text:"Chankheli ", value:"Chankheli" },
                 {text:"Kharpunath ", value:"Kharpunath" },
                 {text:"Simkot ", value:"Simkot" },
                  {text:"Namkha" , value:"Namkha" },
                 {text:"Sarkegad ", value:"Sarkegad" },
                 {text:"Adanchuli ", value:"Adanchuli "},
                 {text:"Tanjakot ", value:"Tanjakot" },


               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Jumla'){
               var municipality =  [



                 {text:"Patarasi" , value:"Patarasi "},
                 {text:"Kanaka Sundari ", value:"Kanaka Sundari" },
                 {text:"Sinja ", value:"Sinja "},
                  {text:"Chandannath", value:"Chandannath"},
                 {text:"Guthichaur" , value:"Guthichaur" },
                 {text:"Tatopani" , value:"Tatopani" },
                 {text:"Tila ", value:"Tila" },
                 {text:"Hima ", value:"Hima" },

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Kalikot'){
               var municipality =  [



                 {text:"Palata ", value:"Palata "},
                 {text:"Pachal Jharana ", value:"Pachal Jharana" },
                 {text:"Raskot", value:"Raskot"},
                  {text:"Sanni Tribeni ", value:"Sanni Tribeni "},
                 {text:"Naraharinath ", value:"Naraharinath "},
                 {text:"Khandachakra", value:"Khandachakra"},
                 {text:"Tilagupha", value:"Tilagupha"},
                 {text:"Mahawai ", value:"Mahawai "},
                 {text:"Kalika ", value:"Kalika "},

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Dailekh'){
               var municipality =  [



                 {text:"Naumule ", value:"Naumule" },
                 {text:"Mahabu ", value:"Mahabu "},
                 {text:"Bhairabi ", value:"Bhairabi" },
                  {text:"Thantikandh ", value:"Thantikandh "},
                 {text:"Aathbis", value:"Aathbis"},
                 {text:"Chamunda Bindrasaini", value:"Chamunda Bindrasaini"},
                 {text:"Dullu", value:"Dullu"},
                 {text:"Narayan", value:"Narayan"},
                 {text:"Bhagawatimai ", value:"Bhagawatimai "},
                 {text:"Dungeshwor ", value:"Dungeshwor" },
                 {text:"Gurans ", value:"Gurans "},

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Jajarkot'){
               var municipality =  [



                 {text:"Barekot ", value:"Barekot" },
                 {text:"Kuse" , value:"Kuse" },
                 {text:"Junichande ", value:"Junichande" },
                  {text:"Chhedagad", value:"Chhedagad"},
                 {text:"Shivalaya ", value:"Shivalaya "},
                 {text:"Bheri Malika", value:"Bheri Malika"},
                 {text:"Tribeni Nalagad", value:"Tribeni Nalagad"},

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Rukum West'){
               var municipality =  [



                 {text:"Aathabisakot", value:"Aathabisakot"},
                 {text:"Sanibheri" , value:"Sanibheri" },
                 {text:"Banphikot" , value:"Banphikot "},
                 {text:"Musikot", value:"Musikot"},
                 {text:"Tribeni" , value:"Tribeni" },
                 {text:"Chaurjahari", value:"Chaurjahari"},

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Salyan'){
               var municipality =  [



                 {text:"Darma ", value:"Darma "},
                 {text:"Kumakh Malika" , value:"Kumakh Malika" },
                 {text:"Banagad Kupinde", value:"Banagad Kupinde"},
                 {text:"Dhorchaur" , value:"Dhorchaur" },
                 {text:"Bagachour", value:"Bagachour"},
                 {text:"Chhatreshwori ", value:"Chhatreshwori" },
                 {text:"Sharada", value:"Sharada"},
                 {text:"Kalimati ", value:"Kalimati "},
                 {text:"Tribeni" , value:"Tribeni "},
                 {text:"Kapurkot ", value:"Kapurkot "},



               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Surkhet'){
               var municipality =  [



                 {text:"Simta ", value:"Simta "},
                 {text:"Chingad ", value:"Chingad" },
                 {text:"Lekabeshi", value:"Lekabeshi"},
                 {text:"Gurbhakot", value:"Gurbhakot"},
                 {text:"Bheriganga", value:"Bheriganga"},
                 {text:"Birendranagar", value:"Birendranagar"},
                 {text:"Barahatal ", value:"Barahatal" },
                 {text:"Panchapuri", value:"Panchapuri"},
                 {text:"Chaukune ", value:"Chaukune "},

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Bajura'){
               var municipality =  [



                 {text:"Himali" , value:"Himali "},
                 {text:"Gaumul" , value:"Gaumul" },
                 {text:"Budhinanda", value:"Budhinanda"},
                 {text:"Swami Kartik ", value:"Swami Kartik "},
                 {text:"Jagannath ", value:"Jagannath" },
                 {text:"Badimalika", value:"Badimalika"},
                 {text:"Khaptad Chhededaha ", value:"Khaptad Chhededaha" },
                 {text:"Budhiganga", value:"Budhiganga"},
                 {text:"Tribeni", value:"Tribeni"},

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Bajhang'){
               var municipality =  [



                 {text:"Kanda" , value:"Kanda" },
                 {text:"Bungal", value:"Bungal"},
                 {text:"Surma ", value:"Surma" },
                 {text:"Talkot" , value:"Talkot" },
                 {text:"Masta ", value:"Masta "},
                 {text:"Jayaprithbi", value:"Jayaprithbi"},
                 {text:"Chhabis Pathibhara" , value:"Chhabis Pathibhara" },
                 {text:"Durgathali ", value:"Durgathali" },
                 {text:"Kedarsyun" , value:"Kedarsyun" },
                 {text:"Bitthadchir ", value:"Bitthadchir "},
                 {text:"Thalara" , value:"Thalara "},
                {text:"Khaptad Chhanna" , value:"Khaptad Chhanna" },


               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Darchula'){
               var municipality =  [



                 {text:"Byas" , value:"Byas" },
                 {text:"Duhun" , value:"Duhun" },
                 {text:"Mahakali", value:"Mahakali"},
                 {text:"Naugad" , value:"Naugad "},
                 {text:"Apihimal" , value:"Apihimal" },
                 {text:"Marma ", value:"Marma" },
                 {text:"Shailyashikhar", value:"Shailyashikhar"},
                 {text:"Malikarjun ", value:"Malikarjun" },
                 {text:"Lekam" , value:"Lekam" },

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Baitadi'){
               var municipality =  [



                 {text:"Dilasaini ", value:"Dilasaini" },
                 {text:"Dogada Kedar" , value:"Dogada Kedar" },
                 {text:"Puchaundi", value:"Puchaundi"},
                 {text:"Surnaya" , value:"Surnaya" },
                 {text:"Dasharathchand", value:"Dasharathchand"},
                 {text:"Pancheshwor" , value:"Pancheshwor" },
                 {text:"Shivanath ", value:"Shivanath "},
                 {text:"Melauli", value:"Melauli"},
                 {text:"Patan", value:"Patan"},
                 {text:"Sigas" , value:"Sigas" },

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Dadeldhura'){
               var municipality =  [



                 {text:"Nawadurga" , value:"Nawadurga" },
                 {text:"Amargadhi", value:"Amargadhi"},
                 {text:"Ajayameru" , value:"Ajayameru" },
                 {text:"Bhageshwor" , value:"Bhageshwor" },
                 {text:"Parashuram", value:"Parashuram"},
                 {text:"Aalital" , value:"Aalital" },
                 {text:"Ganyapdhura" , value:"Ganyapdhura" },



               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Doti'){
               var municipality =  [



                 {text:"Purbichouki" , value:"Purbichouki" },
                 {text:"Sayal" , value:"Sayal" },
                 {text:"Aadarsha" , value:"Aadarsha" },
                 {text:"Shikhar", value:"Shikhar"},
                 {text:"Dipayal Silgadhi", value:"Dipayal Silgadhi"},
                 {text:"K.I. Singh" , value:"K.I. Singh" },
                 {text:"Bogatan" , value:"Bogatan" },
                 {text:"Badi Kedar" , value:"Badi Kedar" },
                 {text:"Jorayal" , value:"Jorayal" },




               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Achham'){
               var municipality =  [



                 {text:"Panchdebal Binayak", value:"Panchdebal Binayak"},
                 {text:"Ramaroshan" , value:"Ramaroshan" },
                 {text:"Mellekh" , value:"Mellekh" },
                 {text:"Sanphebagar", value:"Sanphebagar"},
                 {text:"Chaurpati" , value:"Chaurpati" },
                 {text:"Mangalsen", value:"Mangalsen"},
                 {text:"Bannigadhi Jayagadh" , value:"Bannigadhi Jayagadh" },
                 {text:"Kamal Bazar", value:"Kamal Bazar"},
                 {text:"Dhakari" , value:"Dhakari" },
                 {text:"Turmakhand" , value:"Turmakhand" },




               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Kailali'){
               var municipality =  [



                 {text:"Mohanyal" , value:"Mohanyal" },
                 {text:"Chure" , value:"Chure" },
                 {text:"Godawari", value:"Godawari"},
                 {text:"Gauriganga", value:"Gauriganga"},
                 {text:"Ghodaghodi", value:"Ghodaghodi"},
                 {text:"Bardagoriya" , value:"Bardagoriya" },
                 {text:"Lamki Chuha", value:"Lamki Chuha"},
                 {text:"Janaki" , value:"Janaki" },
                 {text:"Joshipur" , value:"Joshipur" },
                 {text:"Tikapur", value:"Tikapur"},
                 {text:"Bhajani", value:"Bhajani"},
                 {text:"Kailari" , value:"Kailari" },
                 {text:"Dhangadhi ", value:"Dhangadhi "},

               ]

                removeOption()

                appendOption()
            }else if(selectedProvince==='Kanchanpur'){
               var municipality =  [



                 {text:"Krishnapur", value:"Krishnapur"},
                 {text:"Shuklaphanta", value:"Shuklaphanta"},
                 {text:"Bedkot", value:"Bedkot"},
                 {text:"Bhimdatta", value:"Bhimdatta"},
                 {text:"Mahakali", value:"Mahakali"},
                 {text:"Laljhadi" , value:"Laljhadi" },
                 {text:"Punarbas", value:"Punarbas"},
                 {text:"Belouri", value:"Belouri"},
                 {text:"Beldandi" , value:"Beldandi" },


               ]

                removeOption()

                appendOption()
            }


    }
    });