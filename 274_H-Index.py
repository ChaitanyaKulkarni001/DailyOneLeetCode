def checker():
  citations.sort(reverse=True)
  h_index = 0
  for i, citation in enumerate(citations, start=1):
      if i <= citation:
          h_index = i
      else:
          break
  return h_index
