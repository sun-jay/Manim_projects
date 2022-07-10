import numpy as np
import math
#
class CreateGraph(Scene):
    axes = Axes(x_range=[-6, 6],y_range=[-6, 6], axis_config={"color": BLUE},).add_coordinates()
    def ret_eval_str(self,n):
        string = ""
        for i in range(0,n):
            string+= "x**("+str(i)+")/(math.factorial("+str(i)+"))" + "+"
        return string[:-1]
    def ret_graph_label(self,n):
        string = "y= "
        for i in range(0,n):
            string+= "{x^{"+str(i)+"}\over{"+str(i)+"!}} +" 
        return string[:-1]
    def graph_series(self,n):
        graph = self.axes.plot((lambda x: eval(self.ret_eval_str(n))), color=WHITE)
        print(self.ret_eval_str(n))
        print( (lambda x: eval(self.ret_eval_str(n))) (1)  )
        print( self.ret_graph_label(n))
        graph_text = MathTex(self.ret_graph_label(n), font_size=33).shift(UP, RIGHT*4)
        return (graph, graph_text)
    #sin
    def ret_eval_str_sin(self,n):
        string = ""
        for i in range(0,n+1):
            string+= "(-1)**(" + str(i) + ")*x**("+str( (2*i)+1 )+")/(math.factorial("+str( (2*i)+1 )+"))" + "+"
        return string[:-1]
    def ret_graph_label_sin(self,n):
        string = "y= "
        for i in range(0,n+1):

            string += "{(-1)^{"+str(i)+"} {x^{"+str(2*i)+"+1} \over ("+str(2*i)+"+1)!}}+"
        return string[:-1]
    def graph_series_sin(self,n):
        graph = self.axes.plot((lambda x: eval(self.ret_eval_str_sin(n))), color=WHITE)
        print(self.ret_eval_str_sin(n))
        print( (lambda x: eval(self.ret_eval_str_sin(n))) (1)  )
        graph_text = MathTex(self.ret_graph_label_sin(n), font_size=33).shift(UP*3)
        return (graph, graph_text)
    #cos
    def ret_eval_str_cos(self,n):
        string = ""
        for i in range(0,n+1):
            string+= "(-1)**(" + str(i) + ")*x**("+str( (2*i) )+")/(math.factorial("+str( (2*i) )+"))" + "+"
        return string[:-1]
    def ret_graph_label_cos(self,n):
        string = "y= "
        for i in range(0,n+1):

            string += "{(-1)^{"+str(i)+"} {x^{"+str(2*i)+"} \over ("+str(2*i)+")!}}+"
        return string[:-1]
    def graph_series_cos(self,n):
        graph = self.axes.plot((lambda x: eval(self.ret_eval_str_cos(n))), color=WHITE)
        print(self.ret_eval_str_cos(n))
        print( (lambda x: eval(self.ret_eval_str_cos(n))) (1)  )
        graph_text = MathTex(self.ret_graph_label_cos(n), font_size=33).shift(UP*3)
        return (graph, graph_text)
    def ret_eix_str(self,n):
        string = "{{ {( ix )^0\over {0!} }  }}+"
        for n in range(1,n):
            string += "{{ {( ix )^" + str(n) + "\over {" + str(n) + "!} } }}+"
        return string[:-1]
        
    def construct(self):
        def quote():
            form = MathTex("e^", "{\pi", " i}", "+1", "=", "0")
            
            quote = Text("Gentlemen, that is surely true, it is absolutely paradoxical; we cannot understand it,", font_size=17).shift( LEFT)
            quote2 = Text(" and we don't know what it means. But we have proved it, and therefore we know it must be the truth.", font_size=17).shift(DOWN, LEFT)
            name = Text("-  Benjamin Peirce", font_size=20).shift(DOWN*2, LEFT)
            
            text = VGroup(quote, quote2, name) 
            text.arrange(DOWN, center=False, aligned_edge=LEFT) 
            
            self.play(FadeIn(text[0], text[1], form.shift(UP*2)))
            self.wait(6)
            self.play(FadeIn(text[2]))
            
            self.wait(1)
            self.play(FadeOut(text))
            one = MathTex("e^", "{\pi", " i}", "+1", "=", "0")
            one[1].set_color(YELLOW)
            self.play(Transform(form,one))
            self.wait(2)

            
        # quote()
            
# Title
        # title = Text("Understanding")
        # equation = MathTex(
        #     r" e^{ix} = cos(x) + isin(x)"
        # )
        # title2 = Text("in the context of infinte sums")
        # self.play(FadeIn(equation))
        # self.play(FadeIn(title.shift(UP)))
        # self.play(FadeIn(title2.shift(DOWN)))
        # self.wait(3)
        # self.play(FadeOut(equation, title, title2))
        def graph_ex_sum():
            axes = Axes(x_range=[-6, 6],y_range=[-6, 6], axis_config={"color": BLUE},).add_coordinates()
            graph_old = graph = axes.plot(lambda x: 1, color=WHITE)
            graph_text_old = MathTex(self.ret_graph_label(1), font_size=33).shift(UP, RIGHT*4)
            summationLabel = MathTex('y = e^{x} = \sum_{n=0}^{\infty}{x^{n} \over n!}').shift(DOWN*2, RIGHT*3)

            dot_axes = Dot(axes.coords_to_point(1,2.71828), color=GREEN)
            lines = axes.get_lines_to_point(axes.c2p(1,2.71828))
            dotLabel = Text("(1, 2.71828)", font_size=25).next_to(dot_axes, DR)

            self.play(Create(axes), FadeIn(summationLabel))
            self.wait(1)
            self.play( Create(graph_old), FadeIn(graph_text_old))
            self.wait(1)
            for n in range(2,20):
                graph = self.graph_series(n)[0]
                if n<5:
                    graph_text = self.graph_series(n)[1]
                else:
                    graph_text = MathTex(self.ret_graph_label(5)+ "...", font_size=30).shift(UP, RIGHT*4)
                self.play(ReplacementTransform(graph_old, graph,  run_time=2/n), ReplacementTransform(graph_text_old, graph_text,  run_time=2/n))
                graph_old = graph
                graph_text_old = graph_text
                if n<5:
                    self.wait(1)
            self.play(Transform(graph_text, MathTex("y = e^{x}", font_size=30).shift(UP, RIGHT*4)))
            self.wait(1)
            self.play(FadeOut(graph_text), (FadeIn(dot_axes, lines, dotLabel)))
            self.wait(4)
            self.play(FadeOut(dot_axes, lines, dotLabel, axes, graph, summationLabel ))
            self.wait(1)
        #graph_ex_sum()
            
        def graph_sin_sum():
            axes = Axes(x_range=[-3, 3],y_range=[-6, 6], axis_config={"color": BLUE},).add_coordinates().shift(DOWN*0.7)
            graph_old = graph = axes.plot(lambda x: eval(self.ret_eval_str_sin(0)), color=WHITE) 
            graph_text_old = MathTex(self.ret_graph_label_sin(0), font_size=33).shift(UP*3, RIGHT*2)
            summationLabel = MathTex('sin(x) = \sum_{n=0}^{\infty}{(-1)^{n} {x^{2n+1} \over (2n+1)!}}', font_size=33).shift(DOWN*2, RIGHT*3)

            #dot_axes = Dot(axes.coords_to_point(1,2.71828), color=GREEN)
            #lines = axes.get_lines_to_point(axes.c2p(1,2.71828))
            #dotLabel = Text("(1, 2.71828)", font_size=25).next_to(dot_axes, DR)

            self.play(Create(axes), FadeIn(summationLabel))
            self.wait(1)
            self.play( Create(graph_old), FadeIn(graph_text_old))
            self.wait(1)
            for n in range(1,10):
                graph = self.graph_series_sin(n)[0].shift(DOWN*0.7)
                if n<4:
                    graph_text = self.graph_series_sin(n)[1]
                else:
                    graph_text = MathTex(self.ret_graph_label_sin(4)+ "...", font_size=30).shift(UP*3)
                self.play(ReplacementTransform(graph_old, graph,  run_time=2/n), ReplacementTransform(graph_text_old, graph_text,  run_time=2/n))
                graph_old = graph
                graph_text_old = graph_text
                if n<5:
                    self.wait(1)
            self.play(Transform(graph_text, MathTex("y = sin(x)", font_size=30).shift(UP*3 )))
            self.wait(1)
            self.play(FadeOut(graph, axes) ,FadeOut(summationLabel), FadeOut(graph_text))
            self.wait(1)
        graph_sin_sum()
        def graph_cos_sum():
            axes = Axes(x_range=[-3, 3],y_range=[-6, 6], axis_config={"color": BLUE},).add_coordinates().shift(DOWN*0.7)
            graph_old = graph = axes.plot(lambda x: eval(self.ret_eval_str_cos(0)), color=WHITE) 
            graph_text_old = MathTex(self.ret_graph_label_cos(0), font_size=33).shift(UP*3, RIGHT*2)
            summationLabel = MathTex('cos(x) = \sum_{n=0}^{\infty}{(-1)^{n} {x^{2n} \over (2n)!}}', font_size=33).shift(DOWN*2, RIGHT*3)

            #dot_axes = Dot(axes.coords_to_point(1,2.71828), color=GREEN)
            #lines = axes.get_lines_to_point(axes.c2p(1,2.71828))
            #dotLabel = Text("(1, 2.71828)", font_size=25).next_to(dot_axes, DR)

            self.play(Create(axes), FadeIn(summationLabel))
            self.wait(1)
            self.play( Create(graph_old), FadeIn(graph_text_old))
            self.wait(1)
            for n in range(1,10):
                graph = self.graph_series_cos(n)[0].shift(DOWN*0.7)
                if n<4:
                    graph_text = self.graph_series_cos(n)[1]
                else:
                    graph_text = MathTex(self.ret_graph_label_cos(4)+ "...", font_size=30).shift(UP*3)
                self.play(ReplacementTransform(graph_old, graph,  run_time=2/n), ReplacementTransform(graph_text_old, graph_text,  run_time=2/n))
                graph_old = graph
                graph_text_old = graph_text
                if n<5:
                    self.wait(1)
            self.play(Transform(graph_text, MathTex("y = cos(x)", font_size=30).shift(UP*3 )))
            self.wait(1)
            self.play(FadeOut(graph, axes) ,FadeOut(summationLabel), FadeOut(graph_text))
            self.wait(1)
        graph_cos_sum()
        def show_i_powers():
            
            a= MathTex("i", font_size = 90)
            b= MathTex("i^0", font_size = 90)
            c= MathTex("i^{0} = 1 ", font_size = 90)
            d= MathTex("i^{1} = i", font_size = 90)
            e= MathTex("i^{2} = -1", font_size = 90)
            f= MathTex("i^{3} = -i", font_size = 90)
            g= MathTex("i^{4} = 1", font_size = 90)
            
            one = MathTex("i^x", font_size = 90)
            self.play(FadeIn(a))
            self.wait(1)

            self.play(ReplacementTransform(a, one))
            self.wait(1)
            self.play(ReplacementTransform(one, b))
            self.wait(1)
            self.play(Transform(b, c.shift(UP*2)))
            self.wait(1)
            self.play(Transform(c, d.shift(UP*1)))
            self.wait(1)
            self.play(Transform(d, e.shift(UP*0)))
            self.wait(1)
            self.play(Transform(e, f.shift(DOWN)))
            self.wait(1)
            self.play(Transform(f, g.shift(DOWN*2)))
            self.wait(1)
            self.play(FadeOut(b,c,d,e,f,g))
        # show_i_powers()
        def exp_eix():
            
            ex_sum = MathTex( r"e^{{x}} = \sum_{n=0}^{\infty}{{{x}}^{n}\over n!}",substrings_to_isolate="x")
            ex_sum[1].set_color(YELLOW)
            ex_sum[4].set_color(YELLOW)

            eix_sum = MathTex( r"e^{ {{ix}} } = \sum_{n=0}^{\infty} {{ { ( ix )^n\over {n!} } }} ")
            eix_sum[1].set_color(YELLOW)

            txt = MathTex("ix").shift(UP*1.5)
            print(self.ret_eix_str(2))
            self.play(FadeIn(ex_sum))
            self.wait(1)
            self.play(FadeIn(txt))
            self.wait(1)
            self.play(ReplacementTransform(Group(txt, ex_sum), eix_sum))
            self.wait(1)
            self.play((eix_sum.animate.shift(UP*3)))
            self.wait(1)
            
            print(self.ret_eix_str(9))
            
            prev = MathTex(self.ret_eix_str(0))
            exp = MathTex("")
            self.play(FadeIn(prev))
            for n in range(0,9):
                new = MathTex(self.ret_eix_str(n))
                self.play( ReplacementTransform(prev, new))
                
                prev = new
                exp = new
            self.play((new.animate.shift(UP*1.5)))
            self.wait(1) 
            simp_exp = MathTex("{{ {1 }  }}+{{ { ix } }}-{{ { x^2\over {2!} } }}-{{ {ix^3\over {3!} } }}+{{ { x^4\over {4!} } }}+{{ {ix^5\over {5!} } }}-{{ {x^6\over {6!} } }}-{{ {ix^7\over {7!} }... }}")
            self.play(TransformFromCopy(exp, simp_exp))
            self.wait(2 )
            self.play(FadeOut(exp), simp_exp.animate.shift(UP))
            self.wait(1)
            cos_exp = VGroup(simp_exp[0],simp_exp[3],simp_exp[4],simp_exp[7],simp_exp[8],simp_exp[11],simp_exp[12], MathTex("...").shift(UP))
            
            sin_exp = VGroup(simp_exp[1],simp_exp[2],simp_exp[5],simp_exp[6],simp_exp[9],simp_exp[10],simp_exp[13], simp_exp[14])
            self.play(sin_exp.animate.set_color(RED))
            self.wait(1)
            
            cos_exp_copy1 = cos_exp.copy()
            cos_exp_copy2 = cos_exp.copy().arrange_submobjects().shift(DOWN*1.5, LEFT*3) 
            self.play(ReplacementTransform(cos_exp_copy1, cos_exp_copy2))
            self.wait(1)
            
            sin_exp_copy1 = sin_exp.copy()
            sin_exp_copy2 = sin_exp.copy().arrange_submobjects().shift(DOWN*1.5, RIGHT*3) 
            
            self.play(ReplacementTransform(sin_exp_copy1, sin_exp_copy2))
            sin_exp_copy1.remove()
            cos_exp_copy1.remove()
            sin_exp_factored = MathTex(" {{ i( }}   { { x } } -{ {x^3\over {3!} } }+{ {x^5\over {5!} } } -{ {x^7\over {7!} }... }   )    ")
            sin_exp_f_g = VGroup( MathTex("+i("), MathTex("{ { x } } -{ {x^3\over {3!} } }+{ {x^5\over {5!} } } -{ {x^7\over {7!} }... }"), MathTex(")")).arrange_submobjects().set_color(RED).shift(DOWN*1.5, RIGHT*3)
            self.wait(3)
            self.play(ReplacementTransform(sin_exp_copy2, sin_exp_f_g))
            self.wait(1)
            sin_sum = MathTex('  \sum_{n=0}^{\infty}{(-1)^{n} {x^{2n+1} \over (2n+1)!}}').set_color(RED).shift(DOWN*1.5, RIGHT*3)
            cos_sum = MathTex('\sum_{n=0}^{\infty}{(-1)^{n} {x^{2n} \over (2n)!}}').shift(DOWN*1.5, LEFT*3)
            
            self.play(ReplacementTransform(sin_exp_f_g[1] ,sin_sum), ReplacementTransform(cos_exp_copy2 ,cos_sum))
            sinx = MathTex("sin(x)").set_color(RED).shift(DOWN*1.5, RIGHT*3)
            cosx = MathTex("cos(x)").shift(DOWN*1.5, LEFT*3)
            self.wait(1)
            self.play(ReplacementTransform(sin_sum, sinx))
            self.play(Group(sin_exp_f_g[0], sinx, sin_exp_f_g[2]).animate.arrange_submobjects().set_color(RED).shift(DOWN*1.5, RIGHT*3))
         
            self.play( ReplacementTransform( cos_sum, cosx))
            self.wait(1)

            
        # exp_eix()
