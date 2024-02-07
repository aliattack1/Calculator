import unittest as ut
from interface import simple_interface, advanced_interface
class IntegrationTester(ut.TestCase):

    def test_simple(self):
        # simple_interface
        face = simple_interface(mainer=False)
        face.btn_list["1"].invoke()
        face.btn_list["+"].invoke()
        face.btn_list["1"].invoke()
        face.btn_list["="].invoke()
        self.assertEqual(face.label["text"], "1+1")
        self.assertEqual(face.label2["text"], 2.0)
        face.window.destroy()

        # advanced_interface
        face = advanced_interface(mainer=False)
        face.btn_list["1"].invoke()
        face.btn_list["+"].invoke()
        face.btn_list["1"].invoke()
        face.btn_list["="].invoke()
        self.assertEqual(face.label["text"], "1+1")
        self.assertEqual(face.label2["text"], 2.0)
        face.window.destroy()

        # simple_mem
        face = simple_interface(mainer=False)
        face.btn_list["1"].invoke()
        face.btn_list["+"].invoke()
        face.btn_list["1"].invoke()
        face.btn_list["="].invoke()
        face.btn_list["7"].invoke()
        face.btn_list["*"].invoke()
        face.btn_list["6"].invoke()
        face.btn_list["="].invoke()
        face.btn_list["mem"].invoke()
        self.assertEqual(face.label["text"], "1+1")
        self.assertEqual(face.label2["text"], 2.0)
        face.window.destroy()

        # advanced_mem
        face = advanced_interface(mainer=False)
        face.btn_list["1"].invoke()
        face.btn_list["+"].invoke()
        face.btn_list["1"].invoke()
        face.btn_list["="].invoke()
        face.btn_list["7"].invoke()
        face.btn_list["*"].invoke()
        face.btn_list["6"].invoke()
        face.btn_list["="].invoke()
        face.btn_list["mem"].invoke()
        self.assertEqual(face.label["text"], "1+1")
        self.assertEqual(face.label2["text"], 2.0)
        face.window.destroy()

        # simple_del
        face = simple_interface(mainer=False)
        face.btn_list["1"].invoke()
        face.btn_list["0"].invoke()
        face.btn_list["^"].invoke()
        face.btn_list["3"].invoke()
        face.btn_list["*"].invoke()
        face.btn_list["DEL"].invoke()
        face.btn_list["="].invoke()
        self.assertEqual(face.label["text"], "10^3")
        self.assertEqual(face.label2["text"], 1000.0)
        face.window.destroy()

        # advanced_del
        face = advanced_interface(mainer=False)
        face.btn_list["1"].invoke()
        face.btn_list["0"].invoke()
        face.btn_list["^"].invoke()
        face.btn_list["3"].invoke()
        face.btn_list["*"].invoke()
        face.btn_list["del"].invoke()
        face.btn_list["="].invoke()
        self.assertEqual(face.label["text"], "10^3")
        self.assertEqual(face.label2["text"], 1000.0)
        face.window.destroy()

        # simple_ac
        face = simple_interface(mainer=False)
        face.btn_list["1"].invoke()
        face.btn_list["0"].invoke()
        face.btn_list["AC"].invoke()
        face.btn_list["3"].invoke()
        face.btn_list["*"].invoke()
        face.btn_list["2"].invoke()
        face.btn_list["="].invoke()
        self.assertEqual(face.label["text"], "3*2")
        self.assertEqual(face.label2["text"], 6.0)
        face.window.destroy()

        # advanced_ac
        face = advanced_interface(mainer=False)
        face.btn_list["1"].invoke()
        face.btn_list["0"].invoke()
        face.btn_list["ac"].invoke()
        face.btn_list["3"].invoke()
        face.btn_list["*"].invoke()
        face.btn_list["2"].invoke()
        face.btn_list["="].invoke()
        self.assertEqual(face.label["text"], "3*2")
        self.assertEqual(face.label2["text"], 6.0)
        face.window.destroy()

        # simple_ans
        face = simple_interface(mainer=False)
        face.btn_list["9"].invoke()
        face.btn_list["*"].invoke()
        face.btn_list["6"].invoke()
        face.btn_list["="].invoke()
        face.btn_list["Ans"].invoke()
        face.btn_list["*"].invoke()
        face.btn_list["3"].invoke()
        face.btn_list["^"].invoke()
        face.btn_list["2"].invoke()
        face.btn_list["="].invoke()
        self.assertEqual(face.label["text"], "54.0*3^2")
        self.assertEqual(face.label2["text"], 486.0)
        face.window.destroy()

    def test_themes(self):
        face = simple_interface(mainer=False)
        self.assertEqual(face.btn_list["1"]["background"], face.themes["attack"][0])
        self.assertEqual(face.btn_list["1"]["foreground"], face.themes["attack"][1])

        face.theme_menu.invoke("forest")
        self.assertEqual(face.btn_list["1"]["background"], face.themes["forest"][0])
        self.assertEqual(face.btn_list["1"]["foreground"], face.themes["forest"][1])
        face.theme_menu.invoke("haze")

        self.assertEqual(face.btn_list["1"]["background"], face.themes["haze"][0])
        self.assertEqual(face.btn_list["1"]["foreground"], face.themes["haze"][1])
        face.theme_menu.invoke("ocean")

        self.assertEqual(face.btn_list["1"]["background"], face.themes["ocean"][0])
        self.assertEqual(face.btn_list["1"]["foreground"], face.themes["ocean"][1])
        face.theme_menu.invoke("midnight_sky")
        self.assertEqual(face.btn_list["1"]["background"], face.themes["midnight_sky"][0])
        self.assertEqual(face.btn_list["1"]["foreground"], face.themes["midnight_sky"][1])
        face.theme_menu.invoke("light")
        self.assertEqual(face.btn_list["1"]["background"], face.themes["light"][0])
        self.assertEqual(face.btn_list["1"]["foreground"], face.themes["light"][1])

        face.window.destroy()

    def test_a_themes(self):
        face = advanced_interface(mainer=False)
        face.window.update()
        face.window.update_idletasks()


        self.assertEqual(face.btn_list["1"]["background"], face.themes["attack"][0])
        self.assertEqual(face.btn_list["1"]["foreground"], face.themes["attack"][1])
        for i in face.themes.keys():
            face.window.update()
            face.window.update_idletasks()
            face.theme_menu.invoke(i)
            self.assertEqual(face.btn_list["1"]["background"], face.themes[i][0])
            self.assertEqual(face.btn_list["1"]["foreground"], face.themes[i][1])

        face.window.destroy()





class Integration_keyboaard_tester(ut.TestCase):
    def test_keyboard(self):
        face = simple_interface(mainer=False)
        face.window.update()
        face.window.update_idletasks()
        face.window.event_generate("5")
        face.window.event_generate("*")
        face.window.event_generate("6")
        face.window.event_generate("=")
        self.assertEqual(face.label2["text"], 30.0)
        face.window.destroy()

ut.main(IntegrationTester())
ut.main(Integration_keyboaard_tester())