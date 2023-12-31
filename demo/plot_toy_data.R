library(tidyverse)

colors <- col1 <-list("A" = '#109648', "C" = '#255C99',
                      "G" = '#F7B32B', "T" = '#D62839')



all_files <- list.files(pattern = "toy_data_*")


munge_data <- function(df){
  df %>%
    pivot_longer(c('A','C','G','T'), names_to = "Residue", values_to = "encoding") %>%
    mutate(ID = paste0("(", Reference,
                       ", ", Alternate,
                       ", ", VariantCall, ")")) %>%
    group_by(ID) %>%
    mutate(RowSum = sum(encoding)) %>%
    ungroup()
}


plot_data <- function(df){
  df %>%
    ggplot(aes(x = Residue, y = ID,
               fill = Residue,alpha = encoding,
               label = ifelse(encoding > 0, encoding, ""))) +
    geom_tile(color = "black") +
    geom_text() +
    facet_wrap(Reference ~ ., nrow = 2, scales = "free_y") +
    theme_minimal() +
    xlab("") +
    ylab("") +
    scale_fill_manual(values = colors) +
    scale_alpha_continuous(range = c(0, 1), guide = "none") +
    theme(panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          panel.background = element_blank(),
          plot.background =  element_rect(color = "white", fill = "white"))

}

for (zz in list.files(pattern = "csv")){
  df <- read_csv(zz, show_col_types = F)
  df.2 <- munge_data(df)
  p <- plot_data(df.2)

  ofile <- str_replace(zz, "csv", "png")

  cowplot::save_plot(plot = p, ofile,
                     base_height = 8, base_width = 6)
}

