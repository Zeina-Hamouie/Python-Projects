الصورة المرفقة تُمثل رسمًا بيانيًا يوضح التفاعل بين المستخدم (User) ونظام إدارة المهام الذي يتكون من TaskController، Task، وFile. الرسم يصف كيفية تنفيذ العمليات الأساسية في النظام.



إضافة مهمة جديدة:



المستخدم يرسل add\_task(args) إلى TaskController.



TaskController ينشئ مهمة جديدة، ثم يقوم TaskController بإضافتها المهمة إلى الملف tasks.txt.



&nbsp;



عرض المهام:



المستخدم يرسل display(args) إلى TaskController.



TaskController يقوم باختيار إحدى العمليتين بناءً على الشرط if args.all:



إذا كان args.all صحيحًا، يستدعي list\_all\_tasks().

وإلا، يستدعي list\_tasks().

بعد ذلك، يقوم TaskController بطباعة المهام باستخدام print\_table(tasks).



&nbsp;



تحديد مهمة كمكتملة:



&nbsp;



المستخدم يرسل check\_task(args) إلى TaskController.



TaskController يستدعي list\_all\_tasks() للحصول على قائمة المهام.



ثم يقوم بتحديث حالة المهمة وإرسالها إلى File.



&nbsp;



حذف مهمة:



المستخدم يرسل remove(args) إلى TaskController.



TaskController يستدعي list\_all\_tasks() للحصول على قائمة المهام.



ثم يُعيد كتابة الملف بدون المهمة المحددة.



&nbsp;



مسح جميع المهام:



المستخدم يرسل reset() إلى TaskController.



TaskController يقوم بمسح محتوى الملف tasks.txt.



كملخص نهائي:



المستخدم (User): يمثل الشخص الذي يدير المهام من خلال إصدار الأوامر مثل add\_task، display، check\_task، remove، و reset.



TaskController: هو العقل المدبر الذي ينفذ المنطق البرمجي. يتعامل مع الأوامر ويتفاعل مع ملف التخزين. على سبيل المثال:



يقوم بإنشاء مهمة جديدة.

يدير العرض باستخدام list\_tasks() أو list\_all\_tasks() وprint\_table.

يحدث الملف

File (tasks.txt): يمثل ملف التخزين (tasks.txt) الذي يحتفظ ببيانات المهام ويتم تحديثه أو مسحه بناءً على الأوامر

