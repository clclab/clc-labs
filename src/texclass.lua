-- https://github.com/jgm/pandoc/issues/2106#issuecomment-371508848

function Div(el)
  if el.classes:includes("question") then
    return {  pandoc.RawBlock("latex", "\\begin{question}"),
              el,
              pandoc.RawBlock("latex", "\\end{question}") }

  elseif el.classes:includes("assignment") then
    return { pandoc.RawBlock("latex", "\\begin{assignment}"),
              el,
              pandoc.RawBlock("latex", "\\end{assignment}") }

  elseif el.classes:includes("bonus") then
    return { pandoc.RawBlock("latex", "\\begin{bonus}"),
              el,
              pandoc.RawBlock("latex", "\\end{bonus}") }
   
  elseif el.classes:includes("exercise") then
    return { pandoc.RawBlock("latex", "\\begin{exercise}"),
              el,
              pandoc.RawBlock("latex", "\\end{exercise}") }
  end
end